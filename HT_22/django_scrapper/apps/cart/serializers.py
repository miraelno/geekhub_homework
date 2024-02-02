from rest_framework import serializers



class CartSerializer(serializers.Serializer):
    product_id = serializers.CharField()
    price = serializers.FloatField()
    quantity = serializers.IntegerField()