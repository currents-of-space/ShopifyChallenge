# Generated by Django 3.1.3 on 2020-12-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='IsAvailable',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='IsOnSale',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
