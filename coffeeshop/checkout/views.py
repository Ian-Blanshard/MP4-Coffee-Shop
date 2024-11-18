from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def checkout(request):
    # get stripe keys and assign to variables
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    # if post method process checkout
    if request.method == 'POST':
        # get bag from session
        bag = request.session.get('bag', {})
        # create dictionary with form data
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        # create order form with dictionary
        order_form = OrderForm(form_data)
        # check form validity
        if order_form.is_valid():
            # if form valid save it
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

            # loop through and create order line item
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                # if product doesn't exist show error
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    # delete order and return to bag 
                    order.delete()
                    return redirect(reverse('view_bag'))
            # option to save delivery info
            request.session['save_info'] = 'save-info' in request.POST
            # redirect to checkout success passing the order number to view
            return redirect(reverse('checkout_success', args=[order.order_number]))
        # if form invalid show error
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    # if not post prepare checkout page/form
    else:
        # get bag from session
        bag = request.session.get('bag', {})
        # if no bag show error and redirect
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))
        # get back contents and calculate cost
        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        # convert cost for stripe
        stripe_total = round(total * 100)
        # set up stripe with api key
        stripe.api_key = stripe_secret_key
        # create payment intetn with amount and currency
        print('creating payment intent')
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        # create order form for page
        order_form = OrderForm()
    # error message to check key is set up correctly
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    # render template with form and stripe details
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

def checkout_success(request, order_number):
    """view for succesful checkouts"""
    # check if user wants to save info !!!implement later
    save_info = request.session.get('save_info')
    # get order and assign to variable
    order = get_object_or_404(Order, order_number=order_number)
    # feedback succesful order info to user
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    # reset bag as order successful
    if 'bag' in request.session:
        del request.session['bag']
    # render template with order details
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
