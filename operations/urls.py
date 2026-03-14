from django.urls import path
from . import views

urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),

    path('receipts/', views.receipts_list, name='receipts'),

    path('deliveries/', views.deliveries_list, name='deliveries'),

    path('stock/', views.stock_list, name='stock'),   # ADD THIS
]
from django.urls import path
from . import views

urlpatterns = [

    path("dashboard/", views.dashboard, name="dashboard"),

    path("receipts/", views.receipts_list, name="receipts"),

    path("deliveries/", views.deliveries_list, name="deliveries"),

    path("stock/", views.stock_list, name="stock"),

    path("move-history/", views.move_history, name="move_history"),  # ADD THIS
]