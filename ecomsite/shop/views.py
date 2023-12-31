from django.shortcuts import render
from .models import Products, Order
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

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zipcode=request.POST.get('zipcode','')
        total = request.POST.get('total','')
    
        order = Order(items=items,name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, total=total)
        order.save()

    return render(request, "shop/checkout.html")