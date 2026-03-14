from django.db import models
from products.models import Product


class Receipt(models.Model):

    STATUS = (
        ('DRAFT', 'Draft'),
        ('READY', 'Ready'),
        ('DONE', 'Done')
    )

    reference = models.CharField(max_length=50)

    contact = models.CharField(max_length=200)

    schedule_date = models.DateField()

    status = models.CharField(max_length=20, choices=STATUS, default='DRAFT')

    def __str__(self):
        return self.reference


class ReceiptLine(models.Model):

    receipt = models.ForeignKey(
        Receipt,
        related_name="lines",
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product} ({self.quantity})"


class Delivery(models.Model):

    STATUS = (
        ('DRAFT', 'Draft'),
        ('WAITING', 'Waiting'),
        ('READY', 'Ready'),
        ('DONE', 'Done')
    )

    reference = models.CharField(max_length=50)

    contact = models.CharField(max_length=200)

    schedule_date = models.DateField()

    status = models.CharField(max_length=20, choices=STATUS, default='DRAFT')

    def __str__(self):
        return self.reference


class DeliveryLine(models.Model):

    delivery = models.ForeignKey(
        Delivery,
        related_name="lines",
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product} ({self.quantity})"