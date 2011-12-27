from django.conf import settings

BACKENDS = getattr(settings, 'SOCIAL_BACKENDS', {
    'storage': 'social.backends.RedisBackend',
})

DEFAULT_BACKEND = getattr(settings, 'SOCIAL_DEFAULT_BACKEND', BACKENDS.keys()[0])

QUEUES = getattr(settings, 'SOCIAL_QUEUES', ['other'])

NOTIFICATION_TEMPLATE_PREFIX = getattr(settings, 'SOCIAL_NOTIFICATION_TEMPLATE_PREFIX', 'social/notifications/')

DEFAULT_QUEUE = getattr(settings, 'SOCIAL_DEFAULT_QUEUE', QUEUES[0])

REDIS_PREFIX = getattr(settings, 'SOCIAL_REDIS_PREFIX', 'default:')
