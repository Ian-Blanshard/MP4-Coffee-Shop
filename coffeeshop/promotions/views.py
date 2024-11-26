from django.shortcuts import render
from products.models import Product

def manage_promotions(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'promotions/manage_promotions.html', context)
