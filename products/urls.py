from django.urls import path
from .views import products, basket_add, basket_remove


app_name = 'products'

urlpatterns = [
    path("", products, name='index'),
    path("category/<int:category_id>/", products, name='category'),
    path("page/<int:page>/", products, name='paginator'),
    path("basket/add/<int:product_id>/", basket_add, name='basket_add'),
    path("basket/remove/<int:basket_id>/", basket_remove, name='basket_remove')
] 