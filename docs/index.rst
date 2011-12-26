Welcome to django-social's documentation!
=========================================

Django-social aims to implement common features of social networks. As of 0.1, it is able to notify users via a an ajax widget.

Notifications are fun
---------------------

Emiting a comment notification looks like this::

    from django.contrib.comments.signals import comment_was_posted

    from subscription.examples.yourlabs import Notification

    def comment_notification(sender, comment=None, **kwargs):
        Notification(comment=comment, template='comment_notification', 
            subscribers_of=comment.content_object)).emit()
    comment_was_posted.connect(comment_notification)

And easy to setup
-----------------

::

    pip install django-social
    # or:
    pip install -e git+https://jpic@github.com/yourlabs/django-social.git

Then add to settings.py INSTALLED_APPS: 'social'.

Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

