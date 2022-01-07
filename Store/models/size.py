
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from Store.models import Tshirt
# Create your models here.


# -------------------------size model-------------
class SizeVarient(models.Model):
    SIZES = (
        ('S',"SMALL"),
        ('M',"MEDIUM"),
        ('L',"LARGE"),
        ('XL',"EXTRA LARGE"),
        ('XXL',"EXTRA EXTRA LARGE"),
    )
    Price = models.IntegerField(null=False)
    Tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
    size = models.CharField(choices=SIZES, max_length=5)

    def __str__(self):
        return f'{self.size}'