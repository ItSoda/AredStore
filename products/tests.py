from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)
        self.common_tests(response)

    def common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)


class ProductsListViewTestCase(TestCase):
    # fixtures = ['productcategory.json', 'products.fixtures.product.json']

    def setUp(self):
        self.products = Product.objects.all()

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self.common_tests(response)
        # self.assertEqual(list(response.contenx_data['object_list']), list(self.products[:3]))

    def test_list_with_category(self):
        # category =  ProductCategory.objects.first()
        path = reverse('products:category', kwargs={'category_id': 1})
        response = self.client.get(path)
        self.common_tests(response)

    def common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'ItSoda - Catalog')
        self.assertTemplateUsed(response, 'products/products.html')
