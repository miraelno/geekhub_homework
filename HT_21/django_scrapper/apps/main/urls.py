from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('list/', views.ListProductAPIView.as_view(), name='product_list'),
    path('add/', views.CreateProductAPIView.as_view(), name='add_product'),
    path('detail/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('edit/<pk>/', views.UpdateProductAPIView.as_view(), name='product_edit'),
    path('delete/<pk>/', views.ProductDelete.as_view(), name='product_delete'),
]
