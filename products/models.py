from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=200)

    sku = models.CharField(max_length=50, unique=True)

    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    