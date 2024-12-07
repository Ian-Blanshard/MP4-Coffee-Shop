from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view to return the shopping bag page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a product to the shopping bag """
    # get product from database
    product = Product.objects.get(pk=item_id)
    # get quantity and redirect from post request
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # get bag from session, or create empty one if none exists
    bag = request.session.get('bag', {})
    # if the product is already in the bag, update its quantity
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'added {product.product_name} to your bag',
            extra_tags=add_to_bag)
    # if not already in bag, add product
    else:
        bag[item_id] = quantity
        messages.success(
            request, f'added {product.product_name} to your bag',
            extra_tags=add_to_bag)
    # save bag updates to session
    request.session['bag'] = bag
    # redirect to page user came from
    return redirect(redirect_url)


def update_bag(request, item_id):
    """ update shopping bag quantities """
    # get product for f-string in messages
    product = Product.objects.get(pk=item_id)
    # get bag from session
    bag = request.session.get('bag', {})
    # if post request
    if request.method == 'POST':
        # check whether to delete or edit
        edit = request.POST.get('edit')
        if edit == 'update':
            quantity = int(request.POST.get('quantity', 1))
            # update quantity
            if quantity > 0:
                bag[item_id] = quantity
                messages.success(
                    request, f'Edited the amount of {product.product_name} '
                    f'in your bag. It now contains {quantity}'
                    f' {product.product_name}')
            # if none left in bag pop
            else:
                bag.pop(item_id, None)
                messages.success(
                    request, f'Removed {product.product_name} from your bag')
        elif edit == 'delete':
            # pop item from bag
            bag.pop(item_id, None)
            messages.success(
                request, f'Removed {product.product_name} from your bag')
        # save bag updates to session
        request.session['bag'] = bag
    # redirect to view bag
    return redirect('view_bag')
