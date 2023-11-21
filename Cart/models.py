from django.db import models
from inventory.models import Product

class Basket(models.Model):
    products = models.ManyToManyField(Product)
    name=models.CharField(max_length=32)
    total = models.IntegerField()
    quantity = models.IntegerField()
    shipping_cost = models.FloatField()
    discounts = models.FloatField()

def add_product(self,product):
    self.product.add(product)
    self.save()
    return self

def getTotal(self):
    product=self.product
    total=0
    for product in products:
        total+=product.price
        return total



    
    def __str__(self):
        return self.name

# Create your models here.
