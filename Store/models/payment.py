from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from Store.models import Tshirt
from Store.models import Order
# Create your models here.

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateField(null=False, auto_now_add=True)
    payment_status = models.CharField(max_length=15, default='FAILED')
    payment_id = models.CharField(max_length=60)
    payment_request_id = models.CharField(max_length=60, null=False)


   