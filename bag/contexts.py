from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    Context processor for basket contents, calculates total cost, if
    delivery charges are required and prepares data for shopping bag view
     """
    # create variables
    bag_items = []
    total = 0
    product_count = 0
    # retreive bag from session
    bag = request.session.get('bag', {})
    # loop through each bag item
    for item_id, quantity in bag.items():
        # get item from database
        product = get_object_or_404(Product, pk=item_id)
        # check if discounted and apply discount if needed
        discount = getattr(product, 'discount', None)
        if discount:
            price_after_discount = discount.apply_discount(product.price)
        else:
            price_after_discount = product.price
        # calculate cost for this item
        item_total = quantity * price_after_discount
        total += item_total
        product_count += quantity
        # add details for item to bag items list
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'price_after_discount': price_after_discount,
            'item_total': item_total,
        })
    # calculate delivery costs
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    # calculate grand total
    grand_total = delivery + total
    # prepare context for template
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    return context
