from django.db import models

# Create your models here.
class Delivery_Person(models.Model):
    Delivery_Person_Name=models.CharField(max_length=32)
    location=models.CharField(max_length=32)
    Phone_Number=models.PositiveIntegerField()
    Price=models.PositiveIntegerField()

    def __str__(self):
        return self.name




