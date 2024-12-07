from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """a view to return the profile page"""
    profile = get_object_or_404(UserProfile, user=request.user)
    # if method post check form is valid and save updated details
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            # show success toast
            messages.success(request, 'Profile updated successfully')
    else:
        form = UserProfileForm(instance=profile)
    # get all users orders
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    # save orders and form as context to pass to template
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """a view to access previous user order and view checkout page for it"""
    order = get_object_or_404(Order, order_number=order_number)
    # use toast to notify its a past order
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))
    template = 'checkout/checkout_success.html'
    # save order and flag for being from profile to pass to checkout_success
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
