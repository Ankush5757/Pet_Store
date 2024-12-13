# Generated by Django 5.1.1 on 2024-10-15 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_alter_profile_pic_user'),
        ('App', '0006_alter_cart_grand_total_alter_cart_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('user_token', models.FloatField()),
                ('delivery_token', models.IntegerField()),
                ('address', models.CharField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.pets')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.cust_register')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('payment_id', models.CharField()),
                ('razorpay_payment_id', models.CharField()),
                ('razorpay_order_id', models.CharField()),
                ('razorpay_signature', models.CharField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.pets')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.cust_register')),
            ],
        ),
    ]
