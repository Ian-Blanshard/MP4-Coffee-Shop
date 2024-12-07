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
    # get product from database
    product = get_object_or_404(Product, pk=product_id)
    # assign all reviews to a variable
    reviews = product.reviews.all()
    # save variable to context to pass to template
    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'reviews/product_reviews.html', context)


@login_required
def add_review(request, product_id):
    """ a view to add a review for a product"""
    # get product which review is for
    product = get_object_or_404(Product, pk=product_id)
    # if method post check form is valid and save review
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():

            review = form.save(commit=False)

            review.user = request.user.userprofile
            review.product = product
            review.save()
            # show success toast and redirect to product details
            messages.success(request, "Review Added")
            return redirect('product_detail', product_id=product.id)
        # if form not valid show error
        else:
            messages.error(request,
                           "Please ensure the review form is \
                            filled in correctly")
    # not post request generate review form
    else:
        form = ReviewForm()
    # save context to pass to template
    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'reviews/add_review.html', context)


@login_required
def edit_review(request, review_id):
    """a view to edit reviews for a product"""
    # get review/ product details from database
    review = get_object_or_404(Reviews, pk=review_id)
    product = review.product
    # check if superuser or creator of review, show error if not
    if not (request.user.is_superuser or request.user == review.user):
        messages.error(
            request, "You do not have the authorisation to edit this review")
        return redirect('product_reviews', product_id=review.product.id)
    # if method is post, check form valid and save
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            # show success message and redirect
            messages.success(request, "Review updated")
            return redirect('product_reviews', product_id=review.product.id)
    # not post method generate form, with review filled in
    else:
        form = ReviewForm(instance=review)
    # save context to pass to template
    context = {
        'form': form,
        'review': review,
        'product': product,
    }
    return render(request, 'reviews/edit_review.html', context)


@login_required
def delete_review(request, review_id):
    """a view to delete a review for a product"""
    # get review from database
    review = get_object_or_404(Reviews, pk=review_id)
    # if not superuser show error and redirect
    if not (request.user.is_superuser or request.user == review.user):
        messages.error(
            request, "You do not have the authorisation to delete this review")
        return redirect('product_reviews', product_id=review.product.id)
    # if superuser delete and show message/ redirect to correct view
    else:
        review.delete()
        messages.success(request, "Review Deleted")
        referer = request.META.get('HTTP_REFERER', '')
        if 'view_reviews' in referer:
            return redirect('view_all_reviews')
        else:
            return redirect('product_reviews', product_id=review.product.id)


@login_required
def view_all_reviews(request):
    """a view for superuser to view all reviews"""
    # if not superuser show error and redirect
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    # if superuser get all reviews from database and save as context
    else:
        reviews = Reviews.objects.all()
        context = {
            'reviews': reviews
        }

        return render(request, 'reviews/view_all_reviews.html', context)
