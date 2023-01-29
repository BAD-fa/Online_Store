from django.utils import timezone
from .models import Order
from celery import shared_task


@shared_task
def delete_expire_orders():
    validate_time = timezone.now() - timezone.timedelta(hours=1)
    Order.objects.filter(created_time__lt=validate_time, status__lt=3).distink().delete()
