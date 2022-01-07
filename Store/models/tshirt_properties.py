from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
# Create your models here.




class TshirtProperty(models.Model):
    title = models.CharField(max_length=50, null=False)
    slug = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

class Occasion(TshirtProperty):
    pass

class IdealFor(TshirtProperty):    
    pass
    
class NeckType(TshirtProperty):
    pass
    
class Sleeve(TshirtProperty):
    pass
    
class Brand(TshirtProperty):
    pass

class Color(TshirtProperty):
    pass
    
