# Generated by Django 4.2.1 on 2023-06-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delivery_Management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery_person',
            old_name='Delivery_Person_Name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='delivery_person',
            name='Phone_Number',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='delivery_person',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
