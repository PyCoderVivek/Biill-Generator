# Generated by Django 5.1.1 on 2024-09-20 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0009_product_bill_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_bill',
            old_name='Product',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='product_bill',
            old_name='price',
            new_name='Price',
        ),
        migrations.RemoveField(
            model_name='product_bill',
            name='Bill_date',
        ),
        migrations.RemoveField(
            model_name='product_bill',
            name='Man',
        ),
    ]
