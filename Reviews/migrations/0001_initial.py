# Generated by Django 4.2.1 on 2023-06-20 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sender_Name', models.CharField(max_length=32)),
                ('Message', models.CharField(max_length=32)),
                ('Time_and_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
