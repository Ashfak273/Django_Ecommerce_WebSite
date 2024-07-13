from http.client import HTTPResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
# 27
from . models import *

from django.contrib import messages
# Create your views here.

# 48
from shop.form import CustomUserForm

# 56
from django.contrib.auth import authenticate, login, logout

# 67
import json


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
    # 61 ifuser already loged in 
    if request.user.is_authenticated:
        return redirect('/')
    else: 
        # 57
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Success")
                return redirect('/')  # return to home page
            else:
                messages.error(request, "Invalid User NAme or Password")
                return redirect('/login')
    return render(request, 'shop/login.html')

# 59
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Success")
        return redirect('/')  # return to home page 


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

# 66
def add_to_cart(request):
    # check we get http response or not first | from product details.html js code 
    if request.headers.get('X-Requested-With')=='XMLHttpRequest':
        if request.user.is_authenticated: # load json data if user loged in already
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            user_id=request.user.id

            # check if product available 
            product_status=Product.objects.get(id=product_id)
            if product_status:
                # if product exists check that prod already added to cart for that user
                if Cart.objects.filter(user=user_id, product_id=product_id):
                    return JsonResponse({'status':'Product Already in Cart'}, status=200)
                else:
                    # check exists quantity is > than user need qty
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(user=request.user, product_id=product_id, prouctd_qty=product_qty)
                        return JsonResponse({'status':'Product Add to Cart Success'}, status=200) 
                    else:
                        return JsonResponse({'status':'Product Stock Not Available'}, status=200)
        else:
            return JsonResponse({'status':'login to Add Cart'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)

# 69
def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        context = {
            'cart': cart
        }
        return render(request, 'shop/cart.html', context)
    else:
        return redirect('/')
    
# 74
def remove_cart(request, id):
    cart_item=Cart.objects.get(id=id)
    cart_item.delete()

    return redirect("/cart")

# 77
def favourite(request):
    # check we get http response or not first | from product details.html js code 
    if request.headers.get('X-Requested-With')=='XMLHttpRequest':
        if request.user.is_authenticated: # load json data if user loged in already
            data=json.load(request)
            product_id=data['pid']
            user_id=request.user.id
            Product_status=Product.objects.get(id=product_id)
            if Product_status:
                if Favourite.objects.filter(user=user_id, product_id=product_id):
                    return JsonResponse({'status': 'Product Already in Favourite'}, status=200)
                else:
                    Favourite.objects.create(user=request.user, product_id=product_id)
                    return JsonResponse({'status': 'Product Added to Favourite'}, status=200)
        else:
            return JsonResponse({'status':'login to Add favourite'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)


# 83
def favourite_view_page(request):
    if request.user.is_authenticated:
        favourites=Favourite.objects.filter(user=request.user)
        context = {
            'favourits': favourites
        }
        return render(request, 'shop/favourite_view.html', context)
    else:
        return redirect('/')

# 86
def remove_fav(request, id):
    fav_item=Favourite.objects.get(id=id)
    fav_item.delete()

    return redirect("/favourite_view_page")