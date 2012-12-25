from .forms import OrderForm

def pizza_form(request):
    return {'order_form': OrderForm(), 'magic_number': 42}
