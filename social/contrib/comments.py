from django.db.models import Q
from django.contrib.comments.models import Comment
from django.contrib.comments import signals
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from social.models import Subscription

from social import shortcuts
from social.notification import Notification, Lazy

"""
Example usage:

from social.contrib import comments
comments.signals.comment_was_posted.connect(comments.comments_subscription)
comments.signals.comment_was_posted.connect(
    comments.comment_lazy_template_notification)
"""

class CommentNotification(Notification):
    @classmethod
    def kwargs_factory(cls, comment, **kwargs):
        kwargs.update(
            content=comment.content_object,
            actor=comment.user,
            sent_at=comment.submit_date,
        )
        return kwargs

    @property
    def subscribers(self):
        content_ct = ContentType.objects.get_for_model(self.content)
        actor_ct = ContentType.objects.get_for_model(self.actor)

        return User.objects.filter(
            Q(
                subscription__content_type=content_ct,
                subscription__object_id=self.content.pk
            ) |
            Q(
                subscription__content_type=actor_ct,
                subscription__object_id=self.actor.pk
            )
        ).exclude(pk=self.actor.pk).distinct()

def comments_subscription(sender, comment=None, **kwargs):
    if comment.user:
        Subscription.objects.subscribe(comment.user, comment.content_object)

def comment_notification(sender, comment=None, **kwargs):
    if comment.user:
        shortcuts.emit(CommentNotification,
            comment=comment,
            template='comment')
