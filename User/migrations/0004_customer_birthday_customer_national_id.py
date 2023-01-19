# Generated by Django 4.1.5 on 2023-01-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_address_receiver_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='national_id',
            field=models.PositiveBigIntegerField(max_length=10, null=True),
        ),
    ]
