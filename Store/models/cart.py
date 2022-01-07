
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from Store.models import Tshirt
from Store.models import SizeVarient
# Create your models here.
# -------------------------cart model------------------

class Cart(models.Model):
    sizeVarient = models.ForeignKey(SizeVarient, on_delete=models.CASCADE)
    quantity = IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

