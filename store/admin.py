from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Price', 'Inventory', 'inventory_status' ,'Description','collection')
    list_editable = ('Price', 'Inventory')
    list_filter = ('collection',)
    search_fields = ('Title__istartswith',)
    # prepopulated_fields = {'slug': ('Title',)}
    list_per_page = 10



    @admin.display(ordering='Inventory') #use in order to implement sorting in above of the column in admin page
    def inventory_status(self, Product):
        if Product.Inventory < 30:
            return "Low"
        return "High"





@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('Tittle',)
    search_fields = ('Tittle',)
    list_per_page = 10


@admin.register(models.Promation)
class PromationAdmin(admin.ModelAdmin):
    list_display = ('Description', 'Discount')
    search_fields = ('Description',)
    list_per_page = 10
    list_editable = ('Discount',)
    list_filter = ('Discount',)

@admin.register(models.Customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ('First_name', 'Last_name', 'Email', 'Phone')
    search_fields = ('First_name', 'Last_name')
    list_per_page = 10
    list_editable = ('Email', 'Phone')
    list_filter = ('Email',)


@admin.register(models.ordersItems)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'Quantity',)
    search_fields = ('product',)
    list_per_page = 10
    list_editable = ('Quantity',)
    list_filter = ('product',)


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('created',)
    search_fields = ('created',)
    list_per_page = 10
    list_filter = ('created',)


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('placed_at', 'payment_status', 'customer',)
    search_fields = ('customer',)
    list_per_page = 10
    list_filter = ('payment_status',)
    list_editable = ('payment_status',)


@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'Quantity',)
    search_fields = ('product',)
    list_per_page = 10
    list_editable = ('Quantity',)
    list_filter = ('cart',)


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('city',)
    search_fields = ('city',)
    list_per_page = 10
    list_filter = ('city',)


# admin.site.register(models.Address)
