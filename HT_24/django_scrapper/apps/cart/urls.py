from django.urls import path

from . import views

app_name = "cart"
urlpatterns = [
    path("cart_add/<slug:product_id>/", views.CartCreateAPIView.as_view(), name="cart_add"),
    path("cart_delete/<slug:product_id>/", views.CartDeleteAPIView.as_view(), name="cart_delete"),
    path("cart_clear/", views.CartClearAPIView.as_view(), name="cart_clear"),
    path("cart_qty/<slug:product_id>/<str:action>/", views.CartQuantityAPIView.as_view(), name="cart_qty"),
]
