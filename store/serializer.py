from rest_framework import serializers
from .models import Product, Collection
from decimal import Decimal

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    Title = serializers.CharField(max_length=255)
    Price = serializers.DecimalField(max_digits=6, decimal_places=2)
    Inventory = serializers.IntegerField()
    product_tax = serializers.SerializerMethodField(method_name='get_product_tax')
    collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())


    def get_product_tax(self, product: Product):
        return product.Price * Decimal(0.18)