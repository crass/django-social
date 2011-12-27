import datetime

from django.utils.importlib import import_module
from django.utils import simplejson
from django.contrib.auth.models import User

from ..models import Subscription
from ..settings import *

class BaseBackend(object):
    def emit(self, notification, queues=None):
        if queues is None:
            if hasattr(notification, 'queues'):
                queues = notification.queues
        for queue in queues:
            self.queue(notification, queue)

    def queue(self, notification, queue):
        raise NotImplementedError()

    def move_queue(self, source, destination):
        raise NotImplementedError()

    def get_notifications(self, queue, limit=-1):
        raise NotImplementedError()

    def count_notifications(self, queue):
        raise NotImplementedError()
