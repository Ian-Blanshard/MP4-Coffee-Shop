from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/', views.product_reviews, name='product_reviews'),
    path('add/<int:product_id>/', views.add_review, name='add_review'),
    path('edit/<int:product_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:product_id>/', views.delete_review, name='delete_review'),
    path('view_reviews/<int:user_id>/', views.view_all_reviews, name='view_all_reviews'),

]