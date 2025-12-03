from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import category, Product
from decimal import Decimal

# Um teste para verificar a criação de um Produto. teste 1
# Um teste para verificar a listagem de Produtos. teste 2

class ProductAPITestCase(APITestCase):

    def setUp(self):#isola os testes
        self.category = category.objects.create(name='Eletrônicos')
        self.list_url = reverse('product-list') 
        self.post_data = {
            'name': 'Mouse Sem Fio',
            'price': '85.99',
            'category_id': self.category.id
        }
        
    def test_1(self):
        response = self.client.post(self.list_url, self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['category'], 'Eletrônicos')
        
    def test_2(self):
        Product.objects.create(name='Teclado Mecânico', price=Decimal('450.00'), category=self.category)
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['category'], 'Eletrônicos')

