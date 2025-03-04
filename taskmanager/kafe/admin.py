from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Table)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DishCategory)
admin.site.register(Revenue)