from rest_framework import serializers
from .models import Product
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'brand', 'category', 'link']
        

class AddProductSerializer(serializers.Serializer):
    product_ids = serializers.CharField()
    
    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['product_ids'] = attrs['product_ids'].split(' ')
        return attrs