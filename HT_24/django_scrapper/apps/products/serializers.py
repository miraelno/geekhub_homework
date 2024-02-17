from multiprocessing import Pool

from rest_framework import serializers

from apps.products.models import Product
from apps.products.models import Category
from apps.products.tasks import save_scrapped_data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'brand', 'link']
        read_only_fields = ['id']


class AddProductSerializer(serializers.Serializer):
    product_ids = serializers.CharField()

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['product_ids'] = attrs['product_ids'].split(' ')
        return attrs

    def create(self, validated_data):
        context = {}
        try:
            for id in validated_data["product_ids"]:
                save_scrapped_data.delay(id)
        except Exception:
            context["started"] = False
            return context

        context["started"] = True
        context["product_ids"] = validated_data["product_ids"]

        return context
