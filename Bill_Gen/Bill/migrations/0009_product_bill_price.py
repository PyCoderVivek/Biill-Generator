# Generated by Django 5.1.1 on 2024-09-20 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0008_remove_product_bill_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_bill',
            name='price',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]
