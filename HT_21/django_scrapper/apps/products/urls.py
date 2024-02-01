from django.urls import path

from apps.products.views import ProductCreateView
from apps.products.views import ProductDeleteView
from apps.products.views import ProductUpdateView

app_name = "products"
urlpatterns = [
    path("create/", ProductCreateView.as_view(), name="create-product"),
    path("update/", ProductUpdateView.as_view(), name="update-product"),
    path("delete/", ProductDeleteView.as_view(), name="delete-product"),
]
