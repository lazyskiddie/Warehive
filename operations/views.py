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

from django.shortcuts import render
from products.models import Product

def stock_list(request):

    products = Product.objects.all()

    return render(request, "stock.html", {"products": products})

from django.shortcuts import render
from .models import Receipt, Delivery
from products.models import Product


def dashboard(request):
    return render(request, "dashboard.html")


def receipts_list(request):
    receipts = Receipt.objects.all()
    return render(request, "receipts_list.html", {"receipts": receipts})


def deliveries_list(request):
    deliveries = Delivery.objects.all()
    return render(request, "deliveries_list.html", {"deliveries": deliveries})


def stock_list(request):
    products = Product.objects.all()
    return render(request, "products_list.html", {"products": products})

from django.shortcuts import render

def move_history(request):
    return render(request, "deliveries_list.html")

from django.shortcuts import render
from .models import Product

def dashboard(request):
    return render(request,"dashboard.html")


def products_list(request):
    products = Product.objects.all()
    return render(request,"products_list.html",{"products":products})


def receipts_list(request):
    return render(request,"receipts_list.html")


def deliveries_list(request):
    return render(request,"deliveries_list.html")


def stock_list(request):
    products = Product.objects.all()
    return render(request,"stock_list.html",{"products":products})


def move_history(request):
    return render(request,"deliveries_list.html")