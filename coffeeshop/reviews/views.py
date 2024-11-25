from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product
from .forms import ReviewForm

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


def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            
            review = form.save(commit=False)
            
            review.user = request.user.userprofile 
            review.product = product
            review.save()  
            return redirect('product_detail', product_id=product.id)
        else:
            messages.error(request, "Please ensure the review form is filled in correctly")
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'reviews/add_review.html', context)
    


def edit_review(request):

    return render(request)


def delete_review(request):

    return render(request)


def view_all_reviews(request):

    return render(request)