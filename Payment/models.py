from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from User.models import User
from Product.models import Product


# Cart and Cart Item fields must be similar to Order and Order item
class Order(models.Model):
    STATUS_WAIT_FOR_PAYMENT = 1
    STATUS_FAILED_PAYMENT = 2
    STATUS_PREPARING_TO_SEND = 3
    STATUS_SEND_SHIPMENT = 4
    STATUS_DELIVERED_SHIPMENT = 5
    STATUS_RETURNED = 6
    ORDER_STATUS = ((STATUS_WAIT_FOR_PAYMENT, _('wait for payment')), (STATUS_FAILED_PAYMENT, _('failed payment')),
                    (STATUS_PREPARING_TO_SEND, _('preparing to send')), (STATUS_SEND_SHIPMENT, _('send shipment')),
                    (STATUS_DELIVERED_SHIPMENT, _('delivered shipment')))

    PAYMENT_ONLINE = 1
    PAYMENT_CASH = 2
    PAYMENT_CREDIT = 3
    PAYMENT_TYPE = ((PAYMENT_ONLINE, _('online')), (PAYMENT_CASH, _('cash')), (PAYMENT_CREDIT, _('credit')))

    # fields
    user = models.ForeignKey(User, models.CASCADE, 'orders')
    status = models.PositiveIntegerField(verbose_name=_('status'), default=1, choices=ORDER_STATUS)
    tracking_code = models.PositiveIntegerField(verbose_name=_('tracking code'), auto_created=True, unique=True)
    orders_price = models.PositiveBigIntegerField(verbose_name=_('order price'), default=0)
    payment_type = models.PositiveSmallIntegerField(verbose_name=_('payment type'), choices=PAYMENT_TYPE, default=1)
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name=_('modified time'), auto_now=True)
    is_paid = models.BooleanField(verbose_name=_('is paid'), default=False)

    class Meta:
        db_table = 'order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'


class OrderItem(models.Model):
    is_valid = models.BooleanField(default=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")
    expire_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=1))
    count = models.PositiveSmallIntegerField(default=0)
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name=_('modified time'), auto_now=True)

    class Meta:
        db_table = 'order_item'
        verbose_name = 'order item'
        verbose_name_plural = 'order items'

    def get_price(self):
        return self.product.price * self.count

    def is_available(self):
        product = self.product
        if product.stock < self.count:
            return False
        return True


class OrderSend(models.Model):
    NORMAL_POST = 1
    FAST_POST = 2
    POST_TYPE = ((NORMAL_POST, _('normal')), (FAST_POST, _('fast')))

    order = models.OneToOneField(Order, models.CASCADE, related_name='order_send')
    post_type = models.PositiveSmallIntegerField(verbose_name=_('post type'), default=1, choices=POST_TYPE)
    recipient_first_name = models.CharField(verbose_name=_('recipient first name'), max_length=64)
    recipient_last_name = models.CharField(verbose_name=_('recipient last name'), max_length=64)
    recipient_phone_number = models.PositiveBigIntegerField(verbose_name=_('recipient phone number'),
                                                            validators=[RegexValidator(
                                                                r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.',
                                                                'invalid')]
                                                            )
    address = models.TextField(verbose_name=_('address'))
    send_cost = models.PositiveBigIntegerField(verbose_name=_('send cost'), default=0)
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name=_('modified time'), auto_now=True)
    tracking_code = models.PositiveIntegerField(verbose_name=_('tracking code'), auto_created=True, unique=True)

    class Meta:
        db_table = 'order_ send'
        verbose_name = 'order send'
        verbose_name_plural = 'order sends'


class Gateway(models.Model):
    code = models.PositiveIntegerField(primary_key=True, auto_created=True)
    order_id = models.CharField(verbose_name=_('order_id'), max_length=50)
    amount = models.IntegerField(verbose_name=_('amount'),
                                 validators=[MaxValueValidator(500000000), MinValueValidator(1000)])
    user = models.ForeignKey(User, models.CASCADE, related_name='getway', verbose_name=_('user'),
                             null=True, blank=True)
    order = models.ForeignKey(Order, models.CASCADE, related_name='getway', verbose_name=_('order'))
    call_back = models.CharField(verbose_name=_('call_back'), max_length=2048)
    id = models.CharField(verbose_name=_('payment_id'), blank=True, null=True)
    payment_link = models.CharField(verbose_name=_('payment_link'), blank=True, null=True, max_length=2048)
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated time'), auto_now=True)


class Payment(models.Model):
    code = models.PositiveIntegerField(primary_key=True, auto_created=True)
    order = models.ForeignKey(Order)
    status = models.PositiveIntegerField(verbose_name=_('status'), default=1)
    track_id = models.PositiveIntegerField(verbose_name=_('track_id'), null=True, blank=True)
    payment_id = models.CharField(verbose_name=_('payment_id'), blank=True, null=True, unique=True)
    order_id = models.CharField(verbose_name=_('order_id'), max_length=50)
    amount = models.IntegerField(verbose_name=_('amount'),
                                 validators=[MaxValueValidator(500000000), MinValueValidator(1000)])
    card_no = models.CharField(verbose_name=_('card_no'), max_length=32)
    hashed_card_no = models.CharField(verbose_name=_('hashed_card_no'), max_length=2048)
    data = models.DateTimeField(verbose_name=_('date'), blank=True, null=True)
