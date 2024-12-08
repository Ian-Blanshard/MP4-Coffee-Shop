from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """
    return render(request, 'core/index.html')

def custom_404(request, exception=None):
    """a view for 404 errors"""
    return render(request, '404.html', status=404)

def custom_500(request):
    """a view for 500 errors"""
    return render(request, '500.html', status=500)
