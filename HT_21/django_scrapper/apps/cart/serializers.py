from rest_framework import serializers

from apps.cart.models import Cart


class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ['id']
