# Generated by Django 5.1.1 on 2024-10-10 05:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_pic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.cust_register'),
        ),
    ]
