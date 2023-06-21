from django.db import models

# Create your models here.

class Orders(models.Model):
    order_id=models.CharField(max_length=32)
    placement=models.DateTimeField(auto_now_add = True)
    order_status=models.CharField(max_length=32)
    number_of_orders=models.PositiveIntegerField()
    total_amount=models.PositiveIntegerField()


    def __str__(self):
        return self.name

