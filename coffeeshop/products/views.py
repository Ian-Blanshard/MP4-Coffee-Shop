from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower
# Create your views here.

def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    # for loading page without query
    query = None
    sort = None
    direction = None
    category = None
    # set default sort key
    sortkey = 'id'

    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            products = products.annotate(lower_name=Lower('product_name'))

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        products = products.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category']
            if Category.objects.filter(name=category).exists():
                products = products.filter(category__name=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            # use Q to search if query is in either name or description
            queries = Q(product_name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
        'selected_category': category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show all a single products details"""

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)