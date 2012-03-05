import datetime

try:
    from django.utils.timezone import now
except ImportError:
    now = datetime.datetime.now

from notification import Notification, Lazy, Variable

def factory(*args, **kwargs):
    if len(args) == 0:
        cls = Notification
    else:
        cls = args[0]

    if getattr(cls, 'kwargs_factory', False):
        kwargs = cls.kwargs_factory(**kwargs)
    
    for key, value in kwargs.items():
        if value:
            kwargs[key] = Lazy(value)

    if 'timestamp' not in kwargs.keys() and 'sent_at' not in kwargs.keys():
        kwargs['sent_at'] = now()

    return cls(**kwargs)

def emit(*args, **kwargs):
    return factory(*args, **kwargs).emit()
