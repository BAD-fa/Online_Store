from django.contrib import admin
from .models import *


class AdminAddress(admin.ModelAdmin):
    list_display = ('customer', 'city', 'province', 'is_valid')
    list_filter = ('is_valid',)


class AdminCustomer(admin.ModelAdmin):
    list_display = ('national_id',)
    list_filter = ('national_id',)


admin.site.register(Address, AdminAddress)
admin.site.register(Customer, AdminCustomer)
