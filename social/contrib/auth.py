from django.db.models import signals
from django.contrib.auth.models import User

from social.models import Subscription

"""
Example usage:

from subscription.contrib.yourlabs.apps import auth
auth.signals.post_save.connect(auth.subscribe_user_to_himself, sender=auth.User)
auth.subscribe_existing_users_to_themselves()
"""

def subscribe_user_to_himself(sender, **kwargs):
    user = kwargs.pop('instance')
    Subscription.objects.subscribe(user, user)

def subscribe_existing_users_to_themselves(sender, 
    **kwargs):
    """
    Example usage:

    auth.signals.post_syncdb.connect(
        auth.subscribe_existing_users_to_themselves)
    """
    for user in User.objects.all():
        Subscription.objects.subscribe(user, user)
