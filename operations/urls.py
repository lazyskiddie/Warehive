from django.urls import path
from . import views

urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),

    path('receipts/', views.receipts_list, name='receipts'),

    path('deliveries/', views.deliveries_list, name='deliveries'),

]