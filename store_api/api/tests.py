# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product, Category

class ProductAPITests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Camisetas') 
        self.list_url = reverse('product-list')

    def test_create_product(self):
        data = {
            'name': 'Camiseta Preta',
            'description': '100% Algodão, tamanho M, corte slim',
            'price': '59.90',
            'category': self.category.id,
        }
        response = self.client.post(self.list_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(response.data['category_name'], 'Camisetas')

    def test_list_products(self):
        Product.objects.create(
            name='Regata',
            description='Tecido Dry-fit',
            price='39.90',
            category=self.category
        )
        response = self.client.get(self.list_url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)