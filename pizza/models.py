from django.db import models

class Pizza(models.Model):
    name = models.CharField('Name', max_length=255, default='')
    components = models.ManyToManyField('Component', null=True, blank=True)

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'

    def __unicode__(self):
        return self.name

class Component(models.Model):
    name = models.CharField('Name', max_length=255, default='')

    class Meta:
        verbose_name = 'Pizza component'
        verbose_name_plural = 'Pizza components'

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
    address = models.TextField('Address', default='')
    deliveryman = models.ForeignKey(Deliveryman, blank=True, null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, blank=True, null=True, 
        verbose_name = 'Pizza')
    quantity = models.PositiveIntegerField('Quantity', default=0)
    order = models.ForeignKey(Order, blank=True, null=True)

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'

