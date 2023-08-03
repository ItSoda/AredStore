from rest_framework import fields, serializers

from products.models import Basket, Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name',
                                            queryset=ProductCategory.objects.all())  # It works like forms | serializer

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image', 'category',)


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    sum = fields.FloatField()
    total_sum = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('id', 'product', 'quantity', 'sum', 'total_sum', 'total_quantity', 'created_timestamp',)
        read_only = ('created_timestamp',)

    def get_total_sum(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_sum()

    def get_total_quantity(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_quantity()
