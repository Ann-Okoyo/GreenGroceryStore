from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Delivery_Person(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=32)
    location=models.CharField(max_length=32)
    Phone_Number=models.CharField(max_length=32)
    Price=models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.name




