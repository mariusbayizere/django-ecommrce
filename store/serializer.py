from rest_framework import serializers
from .models import Product, Collection
from decimal import Decimal



# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     Tittle = serializers.CharField(max_length=255)




# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     Title = serializers.CharField(max_length=255)
#     Price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     Inventory = serializers.IntegerField()
#     product_tax = serializers.SerializerMethodField(method_name='get_product_tax')
#     #this will "Displaying only ID of ForeignKey field"
#     # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())
#     #this will "Displaying name of ForeignKey field, means instead of ID it will display the name of collection"
#     # collection = serializers.StringRelatedField()
#     collection = CollectionSerializer()



class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'Tittle']

# we should use Model Serializer in order to displaying all the fields of the model with repeating all Model like above 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'Title', 'Price', 'product_tax' ,'Inventory', 'collection']

    product_tax = serializers.SerializerMethodField(method_name='get_product_tax')



    def get_product_tax(self, product: Product):
        return product.Price * Decimal(0.18)