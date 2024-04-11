from typing import Any
from django.contrib import admin
# from django.db.models.query import QuerySet
from .models import *
# Register your models here.

@admin.register(Category)
class CateogryAdmin(admin.ModelAdmin):
    list_display=['name','product_count']
    search_fields=['name']
    list_per_page=10
    
    def product_count(self,category):
        return category
    
    # def get_queryset(self, request):
    #     return super().get_queryset(request).annotate(
    #         products_count = Count('product')
    #     )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','inventory','discounted_price','category_id','is_sale')
    list_editable=['price']
    list_filter=['category',]
    search_fields=('name',)
    list_per_page=10
    # search_fields=['name','price','category']
    # autocomplete_fields=['category']
       
    def stock(self,product):
        if product.inventory>10:
            return 'In Stock'
        elif product.inventory<10:
            return 'Low Stock'
   
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=(
        'first_name',
        'middle_name',
        'last_name',
        'address',
        'gender',
    )
    search_fileds=('first_name',)
    list_per_page=10


# class OrerItemInline(admin.TabularInline):
class OrerItemInline(admin.StackedInline):
    model=OrderItem
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=(
        "customer",
        "place_at",
        "status_choices",
        "payment_status",
        "shipping_address",
    ) 
    inlines= [OrerItemInline]

# @admin.register(OrderItem)
# class OrderAdmin(admin.ModelAdmin):
#     pass


class CartItemInline(admin.TabularInline):
    model=CartItem    
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=('customer',)
    # autocomplete_fields=('customer',)
    inlines=[CartItemInline]

# @admin.register(CartItem)
# class CartAdmin(admin.ModelAdmin):
#     ist_display=(
#         "cart",
#         "product",
#         "quantity",
#     )