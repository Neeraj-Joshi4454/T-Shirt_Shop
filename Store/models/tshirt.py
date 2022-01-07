from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField

from Store.models import Brand, Color, Occasion, IdealFor, NeckType, Sleeve

class Tshirt(models.Model):
    name = models.CharField(max_length=50, null=False)
    slug = models.CharField(max_length=200, null=False, unique=True, default="")
    description = models.CharField(max_length=500, null=True)
    discount = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'upload/images/', null=False)
    occasion = models.ForeignKey(Occasion, on_delete=models.CASCADE)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Sleeve = models.ForeignKey(Sleeve, on_delete=models.CASCADE)
    neck_type = models.ForeignKey(NeckType, on_delete=models.CASCADE)
    ideal_for = models.ForeignKey(IdealFor, on_delete=models.CASCADE)
    Color = models.ForeignKey(Color, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
