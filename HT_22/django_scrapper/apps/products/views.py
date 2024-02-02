from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.generics import CreateAPIView
from django.shortcuts import redirect, resolve_url

from apps.products.models import Product
from apps.products.serializers import ProductUpdateSerializer
from apps.products.serializers import AddProductSerializer


class ProductCreateView(CreateAPIView):
    serializer_class = AddProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        context = serializer.create(serializer.validated_data)

        return redirect(
            f"{resolve_url('templates:add_product')}"
            f"?started={context['started']}&product_ids={context['product_ids']}"
        )


class ProductUpdateView(mixins.UpdateModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer

    def get_object(self):
        return self.queryset.get(pk=self.request.data['id'])

    def post(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)
        return redirect("templates:product_list")


class ProductDeleteView(mixins.DestroyModelMixin, GenericAPIView):
    queryset = Product.objects.all()

    def get_object(self):
        return self.queryset.get(pk=self.request.data['id'])

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect("templates:product_list")
