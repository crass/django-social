import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

class SubscriptionManager(models.Manager):
    def subscribe(self,user,obj):
        ct = ContentType.objects.get_for_model(obj)
        Subscription.objects.get_or_create(content_type=ct,object_id=obj.pk,user=user)

    def subscribers_of(self, obj):
        ct = ContentType.objects.get_for_model(obj)
        return User.objects.filter(subscription__content_type=ct, 
            subscription__object_id=obj.pk)

class Subscription(models.Model):
    user = models.ForeignKey('auth.User')
    content_type = models.ForeignKey('contenttypes.ContentType')
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    timestamp = models.DateTimeField(editable=False,default=datetime.datetime.now)
    objects = SubscriptionManager()
