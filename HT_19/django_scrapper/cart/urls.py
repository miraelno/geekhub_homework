from django.urls import path

from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart_details, name='cart_details'),
    path('cart_add/<slug:product_id>', views.cart_add, name='cart_add'),
    path('cart_delete/<slug:product_id>', views.cart_delete, name='cart_delete'),
    path('cart_update/<slug:product_id>', views.cart_update, name='cart_update'),
]