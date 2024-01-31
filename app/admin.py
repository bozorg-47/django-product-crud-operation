from django.contrib import admin
from .models import YourModel
from .models import Product

# Register your models here.

class appAdmin(admin.ModelAdmin):
  list_display = ("name", "description",)
admin.site.register(YourModel, appAdmin,)

class productAdmin(admin.ModelAdmin):
  list_display = ("name", "price",)
admin.site.register(Product, productAdmin,)

