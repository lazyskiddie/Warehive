from django.db import models
from products.models import Product
from warehouse.models import Location


class StockMove(models.Model):

    MOVE_TYPE = (
        ('IN', 'Incoming'),
        ('OUT', 'Outgoing')
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField()

    source_location = models.ForeignKey(
        Location,
        related_name='source',
        on_delete=models.CASCADE
    )

    dest_location = models.ForeignKey(
        Location,
        related_name='destination',
        on_delete=models.CASCADE
    )

    move_type = models.CharField(max_length=10, choices=MOVE_TYPE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} {self.move_type} {self.quantity}"
    
