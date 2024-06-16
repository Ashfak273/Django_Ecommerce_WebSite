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
    path('login',login_page, name='login' )
]