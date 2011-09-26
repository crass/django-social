import datetime

from django import template
from django import shortcuts
from django import http
from django.utils import simplejson

import subscription
from subscription.examples.yourlabs.settings import *

def list(request, push_states=None, backend='storage',
    template_name='subscription/examples/yourlabs/list.html', 
    extra_context=None):
    
    if push_states is None:
        push_states = {}

    queues = request.GET.get('queues', 'default').split(';')

    b = subscription.get_backends()[backend]()

    notifications = []
    for queue in queues:
        notifications += b.get_notifications(queue)

        for old_state, new_state in push_states.items():
            b.move_queue(queue, queue.replace(old_state, new_state))

    notifications = sorted(notifications, key=lambda n: n.timestamp)

    context = {
        'notification_list': notifications,
        'today': datetime.date.today()
    }

    context.update(extra_context or {})
    return shortcuts.render(request, template_name, context)

def dropdown_ajax(request, dropdowns=None, states=None, counter_state=None, 
    new_state=None, push_states=None, limit=15, backend='storage',
    template_name='subscription/examples/yourlabs/dropdown.html'):

    if not request.user.is_authenticated():
        return http.HttpResponseForbidden()

    b = subscription.get_backends()[backend]()

    context = {}
    for dropdown in dropdowns:  
        q = 'dropdown=%s,user=%s,%s' % (dropdown, request.user.pk, counter_state)
        count = b.count_notifications(q)
        if count == 0:
            continue

        for old_state, new_state in push_states.items():
            q = 'dropdown=%s,user=%s,%s' % (dropdown, request.user.pk, old_state)
            b.move_queue(q, q.replace(old_state, new_state))

        notifications = []
        for state in states:
            q = 'dropdown=%s,user=%s,%s' % (dropdown, request.user.pk, state)
            notifications += b.get_notifications(queue=q, 
                limit=limit-len(notifications))

        context[dropdown] = template.loader.render_to_string(
        template_name, {
            'notifications': notifications,
            'request': request,
            'dropdown': dropdown,
            'counter': count,
        })

    return http.HttpResponse(simplejson.dumps(context), mimetype='application/javascript')

def dropdown_open(request, push_states=None, backend='storage'):
    dropdown = request.GET['dropdown']
    b = subscription.get_backends()[backend]()

    for old_state, new_state in push_states.items():
        q = 'dropdown=%s,user=%s,%s' % (dropdown, request.user.pk, old_state)
        b.move_queue(q, q.replace(old_state, new_state))
    
    return http.HttpResponse('OK')
