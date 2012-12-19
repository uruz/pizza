from django.http import HttpResponse
from django.template.response import TemplateResponse
#from django.views.generic import ListView
from .models import Pizza

def pizza_list(request):
    pizza_list = Pizza.objects.all()

    return TemplateResponse(request, 'index.html',
        {'pizza_list': pizza_list})
