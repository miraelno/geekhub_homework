from django.urls import path

from . import views

app_name = "cart"
urlpatterns = [
    path("", views.cart_details, name="cart_details"),
    path("cart_add/<slug:product_id>", views.cart_add, name="cart_add"),
    path("cart_delete/<slug:product_id>", views.cart_delete, name="cart_delete"),
    path(
        "cart_decrease_qty/<slug:product_id>",
        views.cart_decrease_qty,
        name="cart_decrease_qty",
    ),
    path(
        "cart_increase_qty/<slug:product_id>",
        views.cart_increase_qty,
        name="cart_increase_qty",
    ),
    path("cart_delete/<slug:product_id>", views.cart_delete, name="cart_delete"),
    path("cart_clear", views.cart_clear, name="cart_clear"),
]
