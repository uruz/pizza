#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import Order, Deliveryman
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CreateOrderForm(forms.Form):
    comment = forms.CharField(label = 'Comment')

class OrderForm(forms.ModelForm):
    comment = forms.CharField(label = 'Comment', required=False,
        widget = forms.Textarea(attrs={'cols':'10', 'rows':'10'}))
    class Meta:
        model = Order
        fields = ('city', 'address', )

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'Order'
        self.helper.add_input(Submit('', 'Submit'))

    def save(self, *args, **kwargs):
        self.instance.deliveryman = Deliveryman.objects.get(name = 'user1')
        return super(OrderForm, self).save(*args, **kwargs)

    def clean(self):
        if self.cleaned_data['city'] == Order.PENZA and \
            not self.cleaned_data['address'].strip():
            raise forms.ValidationError('Please fill in address')
        return self.cleaned_data