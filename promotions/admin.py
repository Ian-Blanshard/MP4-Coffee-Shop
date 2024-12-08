from django.contrib import admin
from .models import Discount


class DiscountAdmin(admin.ModelAdmin):
    fields = ('product', 'percentage', 'discounted_price')
    readonly_fields = ('discounted_price',)
    ordering = ('product',)

    def discounted_price(self, obj):
        return obj.discounted_price()
    discounted_price.short_description = 'Discounted Price'


admin.site.register(Discount, DiscountAdmin)
