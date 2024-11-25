from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.
def product_reviews(request, product_id):
    """ a view to show all reviews for a product"""
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.all()
    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'reviews/product_reviews.html', context)


def add_review(request):

    return render(request)


def edit_review(request):

    return render(request)


def delete_review(request):

    return render(request)


def view_all_reviews(request):

    return render(request)