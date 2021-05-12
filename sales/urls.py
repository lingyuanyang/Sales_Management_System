from django.urls import path

from . import views

urlpatterns = [
    path('orders/', views.list_orders),

    path('customers/', views.list_customers),

]
