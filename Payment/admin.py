from django.contrib import admin
from .models import OrderSend, OrderItem, Order


class OrderSendTabularInline(admin.TabularInline):
    model = OrderSend
    fields = ('post_type', 'recipient_first_name', 'recipient_last_name', 'recipient_phone_number',
              'address', 'send_cost', 'tracking_code')


extra = 0


class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'expire_time', 'count')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = (OrderItemTabularInline, OrderSendTabularInline)
