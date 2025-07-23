from django.contrib import admin
from .models import Category, Product, ProductImage, Order, OrderItem

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')
    list_filter = ('category',)
    search_fields = ('name',)
    inlines = [ProductImageInline]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'status', 'total_price', 'created_at')
    list_filter = ('status',)
    search_fields = ('customer_name', 'customer_email')
    inlines = [OrderItemInline]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
