# Generated by Django 4.2.4 on 2023-09-29 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_orderitem_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='additional_images',
            field=models.ManyToManyField(blank=True, to='store.product'),
        ),
    ]