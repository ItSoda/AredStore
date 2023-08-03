from django.urls import include, path
from rest_framework import routers

from .views import BasketModelViewSet, ProductModelViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', ProductModelViewSet)
router.register(r'basket', BasketModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
