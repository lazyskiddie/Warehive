from django.shortcuts import render
from .models import Receipt, Delivery


def dashboard(request):

    receipts = Receipt.objects.count()

    deliveries = Delivery.objects.count()

    context = {
        "receipts": receipts,
        "deliveries": deliveries
    }

    return render(request, "dashboard.html", context)

