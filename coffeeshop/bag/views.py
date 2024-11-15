from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view to return the shopping bag page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'added {product.product_name} to your bag', extra_tags=add_to_bag)
    else:
        bag[item_id] = quantity
        messages.success(request, f'added {product.product_name} to your bag', extra_tags=add_to_bag)

    request.session['bag'] = bag
    return redirect(redirect_url)

def update_bag(request, item_id):
    """ update shopping bag quantities """

    bag = request.session.get('bag', {})

    if request.method == 'POST':
        edit = request.POST.get('edit')

        if edit == 'update':
            quantity = int(request.POST.get('quantity', 1))
            # update quantity
            if quantity > 0:
                bag[item_id] = quantity
            # if none left in bag pop
            else:
                bag.pop(item_id, None)
        elif edit == 'delete':
            # pop item from bag
            bag.pop(item_id, None)
        
        request.session['bag'] = bag
    
    return redirect('view_bag')