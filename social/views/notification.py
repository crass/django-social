import datetime

from django import template
from django import shortcuts
from django import http
from django.utils import simplejson

import social
from ..settings import *

def list(request, keys=None, states=None, push_states=None,
    backend=DEFAULT_BACKEND, extra_context=None,
    template_name='social/list.html'):

    if not request.user.is_authenticated():
        return http.HttpResponseForbidden()

    b = social.get_backends()[backend]()
    context = {
        'today': datetime.date.today(),
    }
    notifications = context['notification_list'] = []
    for key in keys:
        for state in states:
            queue = '%s,user=%s,%s' % (key, request.user.pk, state)
            context['notification_list'] += b.get_notifications(queue)

        for old_state, new_state in push_states.items():
            b.move_queue(queue, queue.replace(old_state, new_state))

    notifications = sorted(notifications, key=lambda n: n.timestamp)

    context.update(extra_context or {})
    return shortcuts.render(request, template_name, context)
