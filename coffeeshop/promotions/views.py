from django.shortcuts import render

def manage_promotions(request):
    return render(request, 'promotions/manage_promotions.html')
