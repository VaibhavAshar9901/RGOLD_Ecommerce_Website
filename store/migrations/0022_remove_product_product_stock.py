# Generated by Django 3.1.7 on 2021-05-01 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20210430_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_stock',
        ),
    ]
