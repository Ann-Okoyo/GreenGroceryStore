from django.db import models

# Create your models here.
class Shipment(models.Model):
    Portname=models.CharField(max_length=32)
    Date_of_Shipment_Placed=models.DateTimeField(auto_now_add = True)
    Date_of_Receive_Shipment=models.DateTimeField(auto_now_add = True)
    Product=models.CharField(max_length=32)
   
    
    def __str__(self):
        return self.name



