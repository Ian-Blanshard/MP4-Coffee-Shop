from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage_promotions, name='manage_promotions'),
    path('promotions/edit/<int:product_id>/',
         views.edit_discount, name='edit_discount'),
]
