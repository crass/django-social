from django import shortcuts
from django.db.models import signals
from django.contrib.auth.models import User
from social.notification import Notification

# deploy contrib for a quick try
from social.contrib import comments

# auto subscribe users to objects they comment
comments.signals.comment_was_posted.connect(comments.comments_subscription)

# auto notify subscribers of an object when it receives a comment
# full blown, reusable:
# comments.signals.comment_was_posted.connect(comments.comment_notification)

# quickstart example:
def comment_notification(sender, comment=None, **kwargs):
    Notification(comment=comment, template='comment_quickstart',
        subscribers_of=comment.content_object).emit()
comments.signals.comment_was_posted.connect(comment_notification)

from social.contrib import auth
auth.signals.post_save.connect(auth.subscribe_user_to_himself, sender=User)
auth.subscribe_existing_users_to_themselves(None)

def user_detail(request, username,
    template_name='auth/user_detail.html', extra_context=None):
    context = {
        'user': shortcuts.get_object_or_404(User, username=username)
    }
    context.update(extra_context or {})
    return shortcuts.render(request, template_name, context)
