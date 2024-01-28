from django.urls import path

from apps.templates import views

app_name = 'templates'
urlpatterns = [
    path('cart-list/', views.cart_list, name='cart_list'),
    path('product-list/', views.product_list, name='product_list'),
    path('add-product/', views.add_product, name='add_product'),
    path('product-detail/<pk>/', views.product_detail, name='product_detail'),
    # TODO: refactor views
    path('update-product/<pk>/', views.ProductEdit.as_view(), name='update_product'),
    path('delete-product/<pk>/', views.ProductDelete.as_view(), name='delete_product'),
]
