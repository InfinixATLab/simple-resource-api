from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Product

# Create your tests here.

class ProductTests(APITestCase):
    def setUp(self):
        self.categoty = Category.objects.create(name="Electronics")
        self.url = reverse('product-list')

    def test_create_product(self):
        data = {
            'name': 'Mouse Gamer',
            'description': 'High precision gaming mouse',
            'price': '49.99',
            'category': 'Electronics'
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Mouse Gamer')

    def test_list_products(self):
        Product.objects.create(
            name ='Keyboard',
            description ='Mechanical keyboard',
            price ='89.99',
            category = self.categoty
        )

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Keyboard')
        self.assertEqual(response.data[0]['category'], 'Electronics')