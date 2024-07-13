# 3 create this file

# 9
# from . import views
from .views import *

# 6
from django.urls import path
urlpatterns = [
    # 9, 23
    # path('home', home, name='home'),
    path('', home, name='home'),
    # 12
    path('register', register, name='register'),
    # 25
    path('collections', collections, name='collections'),

    # 33
    path('collections/<str:name>', CollectionsView, name='product_collections'),

    # 39 
    path('collections/<str:cname>/<str:pname>', Product_details, name='product_details'),

    # 53
    path('login',login_page, name='login' ),

    # 58
    path('logout',logout_page, name='logout' ),

    # 65 add to cart  url
    path('addtocart', add_to_cart, name='addtocart'),

    # 68
    path('cart', cart_page, name='cart'),

    # 73
    path('remove_cart/<str:id>', remove_cart, name='remove_cart'),

    # 76
    path('favourite', favourite, name="favourite"),

    #82
    path('favourite_view_page', favourite_view_page, name="favourite_view_page"),

    # 85
    path('remove_fav/<str:id>', remove_fav, name='remove_fav'),

]