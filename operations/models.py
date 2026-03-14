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

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='DRAFT'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference