Welcome to django-social's documentation!
=========================================

Django-social aims to implement common features of social networks. As of 0.1,
it is able to notify users via a an ajax widget.

Notifications are fun
---------------------

Emiting a minimal comment notification looks like this::

    from django.contrib.comments.signals import comment_was_posted

    from social.notification import Notification

    def comment_notification(sender, comment=None, **kwargs):
        Notification(comment=comment, template='comment_quickstart', 
            subscribers_of=comment.content_object).emit()
    comment_was_posted.connect(comment_notification)

And easy to setup
-----------------

::

    pip install -e git+https://github.com/yourlabs/django-social.git#egg=social

Then either:

- enter env/src/social/social_example_project and 'runserver' (recommended)
- or add to settings.py INSTALLED_APPS: 'social', and 'syncdb', and proceed to
  full installation

Features
--------

My current plan is:

- continue improving documentation
- stabilize the API:
    - template tags should use django-native-tags to be more flexible
    - 'lazy' kwarg should be dropped, 'prerender' should be added
    - fix remaining (non-comment) contrib examples and implement them in the
      test project
- write unit tests again
- release 1.0

All contribution is welcome !

Contents:

.. toctree::
   :maxdepth: 2

   installation
   notification

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

