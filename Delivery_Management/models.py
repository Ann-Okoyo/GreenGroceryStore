from django.db import models

# Create your models here.
class Delivery_Person(models.Model):
    name=models.CharField(max_length=32)
    location=models.CharField(max_length=32)
    Phone_Number=models.CharField(max_length=32)
    Price=models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.name




