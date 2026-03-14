from django.db import models

class Warehouse(models.Model):

    name = models.CharField(max_length=200)

    short_code = models.CharField(max_length=10, unique=True)

    address = models.TextField()

    def __str__(self):
        return self.name


class Location(models.Model):

    name = models.CharField(max_length=200)

    short_code = models.CharField(max_length=20)

    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name