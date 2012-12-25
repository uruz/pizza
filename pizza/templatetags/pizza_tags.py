from django.template.base import Library
import math

register = Library()

@register.inclusion_tag('templatetags/magic.html', takes_context=True)
def magic_number_tag(context):
    return {'magic_number': context['magic_number']*2}

@register.filter
def pow(value, arg):
    return math.pow(float(value), float(arg))
