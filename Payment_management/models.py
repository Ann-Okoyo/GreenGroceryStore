from django.db import models

# Create your models here.
class Payment(models.Model):
    amount=models.DecimalField(max_digits=6,decimal_places=2)
    date_of_payment=models.DateTimeField(auto_now_add = True)
    pending_payment=models.DecimalField(max_digits=6,decimal_places=2)
    receipt=models.TextField()
    payment_method=models.CharField(max_length=32)

def __str__(self):
        return self.amount






