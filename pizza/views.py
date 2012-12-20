#coding: utf-8
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import ListView, CreateView
from .models import Pizza, Order, Deliveryman
from django.http import Http404
from django import forms
from django.shortcuts import redirect
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.urlresolvers import reverse_lazy

class PizzaListView(ListView):
    model = Pizza
    template_name = 'index.html'
    template_context_name = 'pizza_list'

pizza_list = PizzaListView.as_view()

class MargaritaPizzaListView(PizzaListView):
    def get_queryset(self):
        return super(MargaritaPizzaListView, self).get_queryset().filter(name__icontains = 'аргарита')

margo = MargaritaPizzaListView.as_view()

class CreateOrderForm(forms.Form):
    comment = forms.CharField(label = 'Comment')

class OrderForm(forms.ModelForm):
    comment = forms.CharField(label = 'Comment', widget = forms.Textarea(attrs={'cols':'10', 'rows':'10'}))
    class Meta:
        model = Order
        fields = ('address',)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'Order'
        self.helper.add_input(Submit('', 'Submit'))

    def save(self, *args, **kwargs):
        self.instance.deliveryman = Deliveryman.objects.get(name = 'user1')
        return super(OrderForm, self).save(*args, **kwargs)

class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order.html'
    success_url = reverse_lazy('home')

create_order = CreateOrderView.as_view()

# def create_order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.info(request, form.cleaned_data['comment'])
#             return redirect('home')
#         else:
#             return TemplateResponse(request, 'order.html', {'form': form})
#         #handle form
#     elif request.method == 'GET':
#         form = OrderForm()
#         return TemplateResponse(request, 'order.html', {'form': form})
#     else:
#         raise Http404
        