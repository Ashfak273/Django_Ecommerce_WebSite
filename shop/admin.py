from django.contrib import admin

# 15
from .models import  *
# Register your models here.
admin.site.register(Catagory)
admin.site.register(Product)




# # 16 to return image also in models create a class and pass that to admin
# class CatagoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image', 'desciption')

# admin.site.register(Catagory, CatagoryAdmin)
# admin.site.register(Product)