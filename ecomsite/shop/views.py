from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator 

# Create your views here.

def index(request):
    product_objects = Products.objects.all()
    item_name = request.GET.get("item_name")

    # SEARCH FUNCTIONALITY
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    # PAGINATION
    pagination = Paginator( product_objects, 4 )
    page = request.GET.get('page') # get current page
    product_objects = pagination.get_page(page)

    return render(request, 'shop/index.html', {'product_objects':product_objects})


def detail(request, product_id):
    product_object = Products.objects.get(id=product_id)
    return render(request, 'shop/detail.html', {'product_object':product_object})