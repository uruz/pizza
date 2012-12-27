from __future__ import unicode_literals
from django.core.management.base import NoArgsCommand
from django.core.mail import send_mail
from ...models import Order
from django.template.loader import render_to_string
from django.conf import settings

class Command(NoArgsCommand):
    def handle_noargs(self, **kwargs):
        orders = Order.objects.all()
        mail = render_to_string('mail.txt', {'orders': orders})
        send_mail('New order', mail, 'me@localhost',
            settings.PIZZA_RECIPIENT_LIST)

