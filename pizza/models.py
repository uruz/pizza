#coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.utils.timezone import now
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey

class Pizza(models.Model):
    name = models.CharField(_('Name'), max_length=255, default='')
    components = models.ManyToManyField('Component', null=True, blank=True)

    class Meta:
        verbose_name = _('Pizza')
        verbose_name_plural = _('Pizzas')

    def __unicode__(self):
        return self.name

class Component(models.Model):
    name = models.CharField(_('Name'), max_length=255, default='')

    class Meta:
        verbose_name = _('Pizza component')
        verbose_name_plural = _('Pizza components')

    def __unicode__(self):
        return self.name


class Deliveryman(models.Model):
    name = models.CharField('Name', max_length=255, default='')

    class Meta:
        verbose_name = 'Delivery man'
        verbose_name_plural = 'Delivery men'

    def __unicode__(self):
        return self.name

class Order(models.Model):
    MOSCOW, WARSAW, PENZA, IRKUTSK = range(4)
    CITIES = (
        (MOSCOW, _('Moscow')),
        (WARSAW, _('Warsaw')),
        (PENZA, _('Penza')),
        (IRKUTSK, _('Irkutsk')),
    )
    city = models.PositiveSmallIntegerField(_('City'),
        choices = CITIES, default=PENZA)
    address = models.TextField(_('Address'), default='', blank=True)
    deliveryman = models.ForeignKey(Deliveryman, blank=True, null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __unicode__(self):
        return u'Address: %s' % self.address

class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, blank=True, null=True, 
        verbose_name = 'Pizza')
    quantity = models.PositiveIntegerField('Quantity', default=0)
    order = models.ForeignKey(Order, blank=True, null=True)

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'

class PizzaLogEntry(models.Model):
    object_id = models.PositiveIntegerField('Object id', default=0)
    content_type = models.ForeignKey(ContentType, null=True, blank=False)
    date = models.DateTimeField('Date', null=True, default=now)

    related_object = GenericForeignKey()

    class Meta:
        verbose_name = 'Log Entry'


@receiver(post_save)
def order_post_save(sender, instance, **kwargs):
    if sender != PizzaLogEntry:
        PizzaLogEntry.objects.create(
            object_id = instance.id, 
            content_type = ContentType.objects.get_for_model(sender))
    