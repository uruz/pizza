#coding: utf-8
from __future__ import unicode_literals
from django.test.testcases import TestCase
from django.test import Client
from .models import Order
from django.test.utils import override_settings
from django.utils.translation import ugettext_lazy
from django.core.urlresolvers import reverse

class SimpleTest(TestCase):
    def setUp(self):
        self.order = Order()
        self.order.city = Order.IRKUTSK
        self.client = Client()

    def test_display(self):
        self.assertEqual(self.order.get_city_display(), ugettext_lazy('Irkutsk'))

    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertTrue(response.status_code == 200)
        self.assertTrue('order_form' in response.context)
        #import ipdb; ipdb.set_trace()
        self.assertTrue(b'10000,0' in response.content)
        #self.assertTemplateUsed()


    # @override_settings(LANGUAGE_CODE = 'en')
    # def test_display_english(self):
    #   order = Order()
    #   order.city = Order.IRKUTSK
    #     self.assertEqual(order.get_city_display(), 'Irkutsk')
