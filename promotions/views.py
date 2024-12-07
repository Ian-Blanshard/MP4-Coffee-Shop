from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Discount
from .forms import DiscountForm

@login_required
def manage_promotions(request):
    """
    This view shows all products with their current discounts
    and allows the user to go to a page where they can edit the discount.
    """
    # Load all products
    products = Product.objects.all()

    # Create a dictionary to hold all discounts
    discounts = {discount.product_id: discount for discount in Discount.objects.all()}

    # Create list to hold product data for the context
    product_data = []

    # Loop through all products and get their discount data
    for product in products:
        discount = discounts.get(product.id)
        discounted_price = discount.apply_discount(product.price) if discount else None

        # Append the product data (including the form and discounted price)
        product_data.append({
            'product': product,
            'discount': discount,
            'discounted_price': discounted_price
        })

    # Create context variable for rendering
    context = {'product_data': product_data}

    return render(request, 'promotions/manage_promotions.html', context)


@login_required
def edit_discount(request, product_id):
    """
    This view allows the user to edit the discount for a specific product.
    """
    # Get the product object based on the provided product_id
    product = get_object_or_404(Product, id=product_id)

    # Get the existing discount for this product, if any
    discount = Discount.objects.filter(product=product).first()

    # Initialize the discount form with the existing discount, if applicable
    if request.method == 'POST':
        form = DiscountForm(request.POST)
        if form.is_valid():
            # Get the selected percentage from the form
            percentage = form.cleaned_data['percentage']

            if percentage == 0:
                # If 0%, delete the discount
                if discount:
                    discount.delete()
            else:
                # Otherwise, create or update the discount
                Discount.objects.update_or_create(
                    product=product,
                    defaults={'percentage': percentage}
                )
            # Redirect back to the promotions page after saving
            return redirect('manage_promotions')
    else:
        form = DiscountForm(instance=discount)

    # Get the current discounted price if the product has a discount
    discounted_price = discount.apply_discount(product.price) if discount else None

    # Render the edit discount page
    context = {
        'product': product,
        'form': form,
        'discounted_price': discounted_price
    }
    return render(request, 'promotions/edit_discount.html', context)
