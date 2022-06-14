from django.contrib import admin

from pizza.forms import PizzaForm

from .models import OrderModel

# Register your models here.

# admin.site.register(OrderModel)

class MyModelAdmin(admin.ModelAdmin):
    form = PizzaForm

admin.site.register(OrderModel, MyModelAdmin)

# @admin.register(OrderModel)
# class OrderAdmin(admin.ModelAdmin):
#     list_display= ('pizza', 'size', 'sauce')