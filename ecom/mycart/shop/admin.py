from django.contrib import admin
from .models import Product,Contact,Order,Test

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Test",{"fields":["prod_test"]}),
    ]



admin.site.register(Product)
admin.site.register(Test)
admin.site.register(Contact)
admin.site.register(Order)
# Register your models here.
