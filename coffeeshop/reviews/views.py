from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .forms import ReviewForm
from .models import Reviews

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

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            
            review = form.save(commit=False)
            
            review.user = request.user.userprofile 
            review.product = product
            review.save() 
            messages.success(request, "Review Added")
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
    

@login_required
def edit_review(request, review_id):

    review = get_object_or_404(Reviews, pk=review_id)

    if not (request.user.is_superuser or request.user == review.user):
        messages.error(request, "You do not have the authorisation to edit this review")
        return redirect('product_reviews')

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated")
            return redirect('product_reviews', product_id=review.product.id)
    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'reviews/edit_review.html', context)

@login_required
def delete_review(request, product_id):

    return render(request, product_id)

@login_required
def view_all_reviews(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    else:

        return render(request)