# Generated by Django 4.2.4 on 2024-05-24 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_rename_user_shippingaddress_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name_plural': 'Shipping Addresses'},
        ),
    ]
