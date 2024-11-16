from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    # get keys from settings 
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    # get bag from session
    bag = request.session.get('bag', {})
    # if no bag alert user and redirect to products page
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    # get current bag/total and format amount for stripe
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    # set stripe api key
    stripe.api_key = stripe_secret_key

    # create stripe intent object with amount and currency type
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # create order form with imported form
    order_form = OrderForm()
    # warning to remind if key not set correctly in environment
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
                         Did you forget to set it in your environment?')
        
    # context needed for stripe payments on page
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)
