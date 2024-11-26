from django.contrib import admin

from .models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    fields = ('product', 'user', 'review',
              'rating', 'created_at', 'updated_at')
    
    readonly_fields = ('created_at', 'updated_at', 'user', 'product')

    ordering = ('-updated_at',)

admin.site.register(Reviews, ReviewsAdmin)
