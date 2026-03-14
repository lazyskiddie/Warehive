from django.contrib import admin
from .models import Receipt, ReceiptLine, Delivery, DeliveryLine

admin.site.register(Receipt)
admin.site.register(ReceiptLine)
admin.site.register(Delivery)
admin.site.register(DeliveryLine)