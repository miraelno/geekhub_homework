from django.db import models


class Product(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(max_length=500)
    brand = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
