from django.shortcuts import render
from .models import Receipt, Delivery


def dashboard(request):
    return render(request, "dashboard.html")


def receipts_list(request):
    receipts = Receipt.objects.all()
    return render(request, "receipts.html", {"receipts": receipts})


def deliveries_list(request):
    deliveries = Delivery.objects.all()
    return render(request, "deliveries.html", {"deliveries": deliveries})