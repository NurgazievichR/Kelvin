from django.contrib import admin

from apps.order.models import Order, Address

admin.site.register(Order)
admin.site.register(Address)