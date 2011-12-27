from django.db.models import signals
from django.db.models import get_model

from subscription.contrib.yourlabs import shortcuts
from subscription.contrib.yourlabs.notification import Notification, Lazy

"""
Example usage: 

from subscription.contrib.yourlabs.apps import django_messages
django_messages.signals.post_save.connect(django_messages.message_notification,
    sender=django_messages.Message)
"""

Message = get_model('django_messages', 'message')

def message_notification(sender, instance=None, **kwargs):
    if not kwargs.get('created', False):
        return

    Notification(
        actor=Lazy(instance.sender),
        recipient=Lazy(instance.recipient),
        message=instance, # user can't edit a message, no need to lazy it
        queues=['dropdown=messages,user=%s,undelivered' % instance.recipient.pk],
        template='message',
        lazy=True,
    ).emit()
