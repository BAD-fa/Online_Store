from django.contrib import admin
from .models import OrderSend, OrderItem, Order


class OrderSendTabularInline(admin.TabularInline):
    model = OrderSend
    fields = ('post_type', 'recipient_first_name', 'recipient_last_name', 'recipient_phone_number',
              'address', 'send_cost', 'created_time', 'modified_time', 'tracking_code')


extra = 0


class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'expire_time', 'count', 'created_time', 'modified_time')


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = (OrderItemTabularInline, OrderSendTabularInline)
