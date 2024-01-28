from django.shortcuts import render, redirect
from .utils import get_or_create_session_cart
from .utils import get_product_from_cart
from apps.main.models import Product
from django.contrib.auth.decorators import login_required


@login_required(login_url='/user/login/')
def cart_details(request):
    cart = get_or_create_session_cart(request)
    return render(request, "cart/cart.html", context={"cart": cart})


def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = get_or_create_session_cart(request)
    
    for item in cart:
        if item.get(product_id):
            return cart_increase_qty(request, product_id)

    cart.append(
        {product_id: {"name": product.name, "quantity": 1, "price": str(product.price)}}
    )
    request.session["shopping_cart"] = cart

    return redirect("main:product_list")


def cart_decrease_qty(request, product_id):
    cart = get_or_create_session_cart(request)

    product = get_product_from_cart(cart, product_id)
    
    if product[product_id]["quantity"] <= 1:
        return cart_delete(request, product_id)

    product[product_id]["quantity"] -= 1

    request.session["shopping_cart"] = cart

    return redirect("cart:cart_details")


def cart_increase_qty(request, product_id):
    cart = get_or_create_session_cart(request)

    product = get_product_from_cart(cart, product_id)

    product[product_id]["quantity"] += 1

    request.session["shopping_cart"] = cart

    return redirect("cart:cart_details")


def cart_delete(request, product_id):
    cart = get_or_create_session_cart(request)
    cart_filtered = [item for item in cart if list(item.keys())[0] != product_id]

    request.session["shopping_cart"] = cart_filtered

    return redirect("cart:cart_details")


def cart_clear(request):
    request.session["shopping_cart"] = []

    return redirect("cart:cart_details")
