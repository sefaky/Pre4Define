from django.db import models
from colorfield.fields import ColorField

# Create your models here.

class ColorDefining(models.Model):
    category = models.CharField(max_length=30)
    pegi = models.CharField(max_length=3)
    commentCount = models.CharField(max_length=11)
    downloads = models.CharField(max_length=12)
    ranking = models.CharField(max_length=4)
    firstHex = ColorField()
    secondHex = ColorField()