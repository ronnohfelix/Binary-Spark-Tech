# Generated by Django 4.2.4 on 2024-05-08 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_rename_date_added_orderitem_date_ordered_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Details',
        ),
    ]
