# Generated by Django 4.2.4 on 2024-05-24 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_alter_shippingaddress_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='user',
            new_name='customer',
        ),
    ]
