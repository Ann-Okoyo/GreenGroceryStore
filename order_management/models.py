# from django.db import models
# from customer.models import Customer
# from Cart.models import Basket
# from Shipment_Management.models import Shipment

# # Create your models here.

# class Orders(models.Model):
#     shipment=models.ManyToManyField(Shipment)
#     customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True, blank=True)
#     order_id=models.CharField(max_length=32)
#     placement=models.DateTimeField(auto_now_add = True)
#     order_status=models.CharField(max_length=32)
#     number_of_orders=models.PositiveIntegerField()
#     total_amount=models.PositiveIntegerField()
#     cart=models.ManyToManyField(Basket)


#     def __str__(self):
#         return self.order_id



from django.db import models
from payment.models import Payment
from Cart.models import Basket
from customer.models import Customer


class Order(models.Model):
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Cart = models.OneToOneField(Basket,models.PROTECT, null=True)
    payment = models.OneToOneField(Payment, models.PROTECT , null=True)
    delivery_options = models.CharField(max_length=32)
    delivery_date = models.DateTimeField()

    def __str__(self):
        return f"Order #{self.pk}"