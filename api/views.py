from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from products.models import Basket, Product
from products.serializers import BasketSerializer, ProductSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ('update', 'create', 'destroy',):
            self.permission_classes = (IsAdminUser,)
        return super(ProductModelViewSet, self).get_permissions()


class BasketModelViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        queryset = super(BasketModelViewSet, self).get_queryset()
        return queryset.filter(user=self.request.user)
