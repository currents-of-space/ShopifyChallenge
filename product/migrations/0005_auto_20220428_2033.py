# Generated by Django 3.1.3 on 2022-04-29 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20220428_2033'),
        ('product', '0004_filterproduct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FilterProduct',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]