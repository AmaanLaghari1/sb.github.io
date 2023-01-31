from django.contrib import admin
from .models import Product, OrderItem, Order, Pimage, PlacedOrder, ProRating

admin.site.register([Pimage,])

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'pub_date', 'category', 'sub_category', 'price', 'bulk_quantity', 'bulk_price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'start_date', 'ordered', 'bill_address', 'being_delivered', 'recieved',]
    list_display_links = ['id', 'user', 'bill_address',]
    list_filter = ['ordered', 'being_delivered', 'recieved',]
    search_fields = ['user__username']

@admin.register(PlacedOrder)
class PlacedOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'ordered_item', 'address', 'zip_code']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'item', 'quantity']

@admin.register(ProRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'date_created']
