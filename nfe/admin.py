from django.contrib import admin

from nfe.models import Client, Provider, Product, Order

# Register your models here.


admin.site.register(Client)
admin.site.register(Provider)
admin.site.register(Product)
admin.site.register(Order)
