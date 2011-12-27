import datetime
import logging

try:
   import cPickle as pickle
except:
   import pickle

logger = logging.getLogger('redis')

import redis

from django.db import models

import base
from ..settings import *

class RedisBackend(base.BaseBackend):
    def __init__(self, prefix='subscription:'):
        self.prefix = REDIS_PREFIX + prefix

    @property
    def redis(self):
        if not hasattr(self, '_redis'):
            self._redis = redis.Redis()
        return self._redis

    def queue(self, notification, queue):
        logger.debug('queuing to %s: %s' % (queue, notification))
        self.redis.lpush(self.prefix + queue, pickle.dumps(notification))

    def move_queue(self, source, destination):
        if source == destination:
            # that would result in key deletion
            logger.debug('NOT moving to %s: %s' % (source, destination))
            return
        logger.debug('moving to %s: %s' % (source, destination))

        source = self.prefix + source
        destination = self.prefix + destination

        notifications = self.redis.lrange(source, 0, -1)

        for notification in notifications:
            self.redis.lpush(destination, notification)
            self.redis.lrem(source, notification)

    def get_notifications(self, queue, limit=-1):
        queue = self.prefix + queue

        if limit > 0:
            queue_limit = limit - 1
        elif limit == 0:
            queue_limit = 0
        else:
            queue_limit = limit

        for n in self.redis.lrange(queue, 0, queue_limit):
            try:
                yield pickle.loads(n)
            except models.ObjectDoesNotExist:
                # notification contains a deleted model, pass on it and let
                # redis_purge take care of it
                continue

    def count_notifications(self, queue):
        queue = self.prefix + queue
        return self.redis.llen(queue)
