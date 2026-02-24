from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product, Category

class ProductAPITests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Eletrônicos') 
        self.list_url = reverse('product-list')

    def test_create_product(self):
        data = {
            'name': 'TV Smart LG 55 4K',
            'description': 'Marca: LG | 55 polegadas | 4K UHD | HDR | Wi-Fi integrado | HDMI x3 | USB x2 | Voltagem: Bivolt',
            'price': '2599.90',
            'category': self.category.id,
        }
        response = self.client.post(self.list_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(response.data['category_name'], 'Eletrônicos')

    def test_list_products(self):
        Product.objects.create(
            name='Smartphone Samsung Galaxy A54',
            description='Marca: Samsung | 128GB | 6GB RAM | Tela 6.4" | Câmera Tripla | Android 13',
            price='1599.90',
            category=self.category
        )
        response = self.client.get(self.list_url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)