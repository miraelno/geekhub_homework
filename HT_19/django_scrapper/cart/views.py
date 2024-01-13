from django.shortcuts import render
from .utils import get_or_create_session_cart

from main.models import Product

def cart_details(request):
    cart = get_or_create_session_cart(request)
    print(cart)
    return render(request, 'cart/cart.html', context={'cart':cart})

def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    print(product_id)

def cart_delete(request, product_id):
    pass

def cart_update(request, product_id):
    pass