# Generated by Django 2.2.12 on 2023-07-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0003_orders_cart_orders_shipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]