from django.contrib import admin

from apps.order.models import Order, Address, Street

admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Street)