from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session

from main.models import Product


def cart_details(request):
    cart = request.session.get("shopping_cart")
    return render(request, "cart/cart.html", context={"cart": cart})


def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get("shopping_cart", [])

    for item in cart:
        if item.get(product_id):
            return cart_increase_qty(request, product_id)

    cart.append(
        {product_id: {"name": product.name, "quantity": 1, "price": str(product.price)}}
    )
    request.session["shopping_cart"] = cart

    return redirect("main:product_list")


def cart_decrease_qty(request, product_id):
    cart = request.session.get("shopping_cart")

    for product in cart:
        if product.get(product_id):
            if product[product_id]["quantity"] <= 1:
                return cart_delete(request, product_id)

            product[product_id]["quantity"] -= 1

    request.session["shopping_cart"] = cart

    return redirect("cart:cart_details")


def cart_increase_qty(request, product_id):
    cart = request.session.get("shopping_cart")

    for product in cart:
        if product.get(product_id):
            product[product_id]["quantity"] += 1

    request.session["shopping_cart"] = cart

    return redirect("cart:cart_details")


def cart_delete(request, product_id):
    cart = request.session.get("shopping_cart")
    cart_filtered = [item for item in cart if list(item.keys())[0] != product_id]

    request.session["shopping_cart"] = cart_filtered

    return redirect("cart:cart_details")


def cart_clear(request):
    request.session["shopping_cart"] = []

    return redirect("cart:cart_details")
