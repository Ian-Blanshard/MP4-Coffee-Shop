from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Discount
from .forms import DiscountForm

@login_required
def manage_promotions(request):
    #if POST request
    if request.method == "POST":
        # get product id from request
        product_id = request.POST.get('product_id')
        # get discount percentage from request
        discount_percentage = request.POST.get('percentage')
        # get product details from databsae
        product = get_object_or_404(Product, pk=product_id)

        # if submitted discount is 0
        if int(discount_percentage) == 0:
            # delete discount from that product
            Discount.objects.filter(product=product).delete()
        else:
        # Update or create the discount object with the new percentage
            Discount.objects.update_or_create(
                product=product,
                defaults={'percentage': int(discount_percentage)}
            )
        # reload manage promotions page
        return redirect('manage_promotions')
    else:
        # Load all products 
        products = Product.objects.all()
        # create a dictionary to hold all discounts
        discounts = {}
        # loop through and fill dictionary with product and discount applied
        for discount in Discount.objects.all():
            discounts[discount.product_id] = discount
        # create list to hold product data
        product_data = []
        # loop through all products
        for product in products:
            # get discount assosciated with that product
            discount = discounts.get(product.id)
            # create form for product
            form = DiscountForm(instance=discount, product_id=product.id)
            # get discounted price to display if product has discount 
            discounted_price = (
                discount.apply_discount(product.price) if discount else None
            )
            # add a dictionary for the product containing its form, product details and discounted price
            product_data.append({
                'product': product,
                'form': form,
                'discounted_price': discounted_price,
            })
        # create context variable
        context = {'product_data': product_data}
        # render template with all required item info in context
        return render(request, 'promotions/manage_promotions.html', context)
