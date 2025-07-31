from django.contrib import admin
from .models import Category, Product, ProductImage, Order, OrderItem

from django.utils.html import format_html

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['image_preview']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.image.url)
        return "No Image"

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
admin.site.register(ProductImage)
