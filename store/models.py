from django.db import models

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    amount = models.IntegerField()
