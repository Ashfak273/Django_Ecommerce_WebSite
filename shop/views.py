from http.client import HTTPResponse
from django.shortcuts import render, redirect
# 27
from . models import *

from django.contrib import messages
# Create your views here.

# 48
from shop.form import CustomUserForm

# 8
def home(request):
    # 44 filter trendings to show in home 
    products = Product.objects.filter(trending=1)
    context = {
        'products': products
    }
    return render(request, 'shop/index.html',context )

# 51
def login_page(request):
    return render(request, 'shop/login.html')

# 10
def register(request):
    # 48

    form = CustomUserForm()

    # 50
    if request.method=='POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success")
            return redirect('/login')
    
    context = {
        'form': form
    }

    return render(request, 'shop/register.html', context)

# 24
def collections(request):
    # 27 0 for show , 1 for hide  so filter which is shown here 
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
