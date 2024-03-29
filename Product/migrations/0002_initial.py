# Generated by Django 4.1.5 on 2023-01-15 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='Product.category'),
        ),
    ]
