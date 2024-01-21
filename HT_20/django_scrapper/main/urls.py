from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('list/', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('detail/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('edit/<pk>/', views.ProductEdit.as_view(), name='product_edit'),
    path('delete/<pk>/', views.ProductDelete.as_view(), name='product_delete'),
]
