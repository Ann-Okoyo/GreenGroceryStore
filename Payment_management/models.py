from django.db import models

# Create your models here.
class Payment(models.Model):
    amount=models.PositiveIntegerField()
    date_of_payment=models.DateField(auto_now_add = True)
    pending_payment=models.BooleanField(verbose_name=str)
    receipt=models.CharField(max_length=32)
    payment_method=models.CharField(max_length=32)

def __str__(self):
        return self.name






