
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from Store.models import Tshirt
from Store.models import SizeVarient


class Order(models.Model):
    orderStatus = (
        ('PENDING','Pending'),
        ('PLACED','Placed'),
        ('CANCELED','Canceled'),
        ('COMPLETED','Completed'),
    )
    method = (
        ('COD','Cod'),
        ('ONLINE','Online'),
    )
    order_status = models.CharField(max_length=15, choices=orderStatus)
    payment_method = models.CharField(max_length=15, choices=method)
    shipping_address = models.CharField(max_length=500, null=False)
    phone = models.CharField(max_length=10, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField(null=False)
    date = models.DateField(null=False, auto_now_add=True)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
    size = models.ForeignKey(SizeVarient, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    date = models.DateField(null=False, auto_now_add=True)

