Full installation
=================

Django-social is designed to get you started quickly first. Also, it attemps to
follow best practices including configurability while embeding many
'unlockable' features.

Notifications list
------------------

To include the "dropdown menu" facebook-ish ajax notification widget, load
social_tags.

Then, add an html container (it can be a div, an li, whatever) with classes "dropdown outer <queue name>". For example::

    {% load social_tags %}

    <div class="dropdown outer other">
        {% social_dropdown request 'other' 'undelivered,unacknowledged,acknowledged' 'undelivered,unacknowledged' 15 %}
    </div>

This template tag is subject to being re-done with django-native-tags to allow optionnal arguments.

Javascript
----------

Enable the javascript as such::

    {% get_static_prefix as STATIC_PREFIX %}

    <!-- load jquery, don't copy that if you already have it -->
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js"></script>

    {% if request.user.is_authenticated %}
    <script type="text/javascript" src="{{ STATIC_PREFIX }}social/jquery-implementation.js"></script>
    <script type="text/javascript">
        $(document).ready(function() {
            Subscription.factory('{% url 'social_dropdown_ajax' %}', '{% url 'social_dropdown_open' %}');
        });
    </script>
    {% endif %}
