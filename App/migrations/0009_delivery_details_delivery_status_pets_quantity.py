# Generated by Django 5.1.1 on 2024-10-22 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_alter_delivery_details_pet_alter_payments_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_details',
            name='delivery_status',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='pets',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
