from django.db import models

# 14 inheritance  use to create database table/content and migrate 
import datetime
# to access path to store image
import os

# 46
from django.contrib.auth.models import User

# funct to check pic name  using current time
# and change time to a format, chnage name with time
def getFileName(requst, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time, filename)
    return os.path.join('uploads/', new_filename)


class Catagory(models.Model):
    name=models.CharField(max_length=150, null=False, blank=False)
    image=models.ImageField(upload_to=getFileName, null=True, blank=True)
    desciption=models.TextField(max_length=500, null=False, blank=False)
    status=models.BooleanField(default=False, help_text="0-default, 1-Hidden")
   
    # generate time
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    # to write join query for which catagory is the product, id of catagory shoud be foreignkey for product
    # what happen to product when a category deleted
    catagory=models.ForeignKey(Catagory, on_delete=models.CASCADE)
    name=models.CharField(max_length=150, null=False, blank=False)
    vendor=models.CharField(max_length=150, null=False, blank=False)
    product_image=models.ImageField(upload_to=getFileName, null=True, blank=True)
    quantity=models.IntegerField(null=False, blank=False)
    original_price=models.FloatField(null=False, blank=False)
    selling_price=models.FloatField(null=False, blank=False)
    desciption=models.TextField(max_length=500, null=False, blank=False)
    status=models.BooleanField(default=False, help_text="0-default, 1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default, 1-Trending")
    # generate time
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name