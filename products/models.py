from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    fact = models.TextField(max_length=1024, default='')
    price = models.DecimalField(decimal_places=2, max_digits=4)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


