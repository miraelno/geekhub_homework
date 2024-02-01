from django.shortcuts import redirect
from rest_framework.generics import ListAPIView

from apps.cart.utils import get_or_create_session_cart
from apps.products.models import Product


class BaseCartAPIView(ListAPIView):
    queryset = Product.objects.all()

    def get_object(self):
        return self.queryset.get(id=self.kwargs.get("product_id"))

    def get_serializer_class(self):
        return None


class CartCreateAPIView(BaseCartAPIView):
    def list(self, request, *args, **kwargs):
        product = self.get_object()
        cart = get_or_create_session_cart(request)

        if cart.get(product.id):
            cart[product.id]["quantity"] += 1
        else:
            cart[product.id] = {
                "name": product.name,
                "quantity": 1,
                "price": str(product.price),
            }

        request.session["shopping_cart"] = cart
        return redirect("templates:cart_list")


class CartDeleteAPIView(BaseCartAPIView):
    def list(self, request, *args, **kwargs):
        product = self.get_object()
        cart = get_or_create_session_cart(request)

        cart.pop(product.id, None)

        request.session["shopping_cart"] = cart
        return redirect("templates:cart_list")


class CartClearAPIView(BaseCartAPIView):
    def list(self, request, *args, **kwargs):
        request.session["shopping_cart"] = {}
        return redirect("templates:cart_list")


class CartQuantityAPIView(BaseCartAPIView):
    def list(self, request, *args, **kwargs):
        product = self.get_object()
        cart = get_or_create_session_cart(request)
        decrease = self.kwargs.get("action") == "decrease"

        if decrease:
            if cart[product.id]["quantity"] <= 1:
                cart.pop(product.id, None)

        if cart.get(product.id):
            cart[product.id]["quantity"] -= 1 if decrease else -1

        request.session["shopping_cart"] = cart
        return redirect("templates:cart_list")
