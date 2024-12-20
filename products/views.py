from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from .models import Product, Category
from django.db.models.functions import Lower, Round
from .forms import ProductForm

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
    # query the products rating from reviews model and round rating
    products = products.annotate(avg_rating=Round(Avg('reviews__rating')))
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
        # remove products with no rating if sortkey is rating
        if sortkey == 'avg_rating' or sortkey == '-avg_rating':
            products = products.filter(avg_rating__isnull=False)

        products = products.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category']
            if category == 'special_offers':
                # get all product with current discount applied
                products = products.filter(discount__isnull=False)
            elif Category.objects.filter(name=category).exists():
                products = products.filter(category__name=category)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            # use Q to search if query is in either name or description
            queries = Q(product_name__icontains=query) | Q(
                description__icontains=query)
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
    product = Product.objects.annotate(
        avg_rating=Round(Avg('reviews__rating'))
    ).get(pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """ Add a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm(request=request)
    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.product_name}')
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product  """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    else:
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))
