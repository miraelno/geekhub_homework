from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('detail/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
]
