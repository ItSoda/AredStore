from django.urls import path
from .views import create_order, orders, success

app_name = 'orders'

urlpatterns = [
    path("", orders, name='orders'),
    path("create_order/", create_order, name='create_order'),
    path("success/", success, name="success")
] 