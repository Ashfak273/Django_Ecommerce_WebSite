from http.client import HTTPResponse
from django.shortcuts import render, redirect
# 27
from . models import *

from django.contrib import messages
# Create your views here.

# 8
def home(request):
    return render(request, 'shop/index.html')

# 10
def register(request):
    return render(request, 'shop/register.html')

# 24
def collections(request):
    # 27 0 for show , 1 for hide  so filter which is shown
    catagory=Catagory.objects.filter(status=0)
    context = {
        'catagory': catagory
    } 
    return render(request, "shop/collections.html", context)

# 34
def CollectionsView(request, name):
    # 35
    catagory=Catagory.objects.filter(status=0, name=name).first()
    if (catagory):
        products=Product.objects.filter(catagory=catagory)
        context = {
            'products': products,
            'catagory': catagory,
        } 
        return render(request, "shop/products/index.html", context)
    else:
        messages.warning(request, "No Such Category Found")
        return redirect("collections")

# 40 passing prod, cat name 
def Product_details(request, cname, pname):
    catagory=Catagory.objects.filter(status=0, name=cname).first()
    if (catagory):
        product=Product.objects.filter(catagory=catagory, name=pname).first()
        if (product):
            context = {
                'product': product,
            } 
            return render(request, "shop/products/product_details.html", context)
        else:
            messages.warning(request, "No Such Product Found")
            return redirect("collections")
    else:
        return redirect("collections")
