from django.urls import path

from .views import (CanceledTemplateView, OrderCreateView, OrderDescView,
                    OrderListView, SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path("order_create/", OrderCreateView.as_view(), name='order_create'),
    path("order_success/", SuccessTemplateView.as_view(), name='order_success'),
    path("order_cancel/", CanceledTemplateView.as_view(), name='order_cancel'),
    path('', OrderListView.as_view(), name='orders_list'),
    path('order/<int:pk>/', OrderDescView.as_view(), name='order')
]
