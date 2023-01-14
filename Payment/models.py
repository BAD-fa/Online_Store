from django.db import models
from django.utils.translation import gettext_lazy as _
from User.models import User


# Cart and Cart Item fields must be similar to Order and Order item
class Order(models.Model):
    STATUS_WAIT_FOR_PAYMENT = 1
    STATUS_FAILED_PAYMENT = 2
    STATUS_PREPARING_TO_SEND = 3
    STATUS_SEND_SHIPMENT = 4
    STATUS_DELIVERED_SHIPMENT = 5
    STATUS_RETURNED = 6
    user = models.ForeignKey(User, models.CASCADE, 'orders')
    ORDER_STATUS = ((STATUS_WAIT_FOR_PAYMENT, _('wait for payment')), (STATUS_FAILED_PAYMENT, _('failed payment')),
                    (STATUS_PREPARING_TO_SEND, _('preparing to send')), (STATUS_SEND_SHIPMENT, _('send shipment')),
                    (STATUS_DELIVERED_SHIPMENT, _('delivered shipment')))

    PAYMENT_ONLINE = 1
    PAYMENT_CASH = 2
    PAYMENT_CREDIT = 3
    PAYMENT_TYPE = ((PAYMENT_ONLINE, _('online')), (PAYMENT_CASH, _('cash')), (PAYMENT_CREDIT, _('credit')))
    status = models.PositiveIntegerField(verbose_name=_('status'), default=1)
    taking_code = models.PositiveIntegerField(verbose_name=_('tracking code'), auto_created=True, unique=True)
    order_price = models.DecimalField(verbose_name=_('order price'), max_digits=5, default=0)
    payment_type = models.PositiveSmallIntegerField(verbose_name=_('payment type'), choices=PAYMENT_TYPE, default=1)


class OrderItem(models.Model):
    pass


class Payment(models.Model):
    pass
