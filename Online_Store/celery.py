import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Online_Store.settings')
app = Celery('Online_Store')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://localhost:6379/0'
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete_expire_orders': {
        'task': 'Payment.tasks.delete_expire_orders',
        'schedule': crontab(minute='*/5', hour='*'),
    },
}
