from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    # set which product info is displayed in admin
    list_display = (
        'sku',
        'product_name',
        'price',
        'category',
    )

    # set order by which they appear
    ordering = (
        'sku',
    )

class CategoryAdmin(admin.ModelAdmin):
    # set which product info is displayed in admin
    list_display = (
        'friendly_name',
        'name'
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)