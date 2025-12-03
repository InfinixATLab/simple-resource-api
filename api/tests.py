from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Category, Product


class ProductTest(APITestCase):
  def setUp(self):
    self.category = Category.objects.create(name = "Eletrônicos")
    self.product_data = {
      "name":"teclado gamer",
      "description":"teclado 100% padrão ABNT2",
      "price":"90.00",
      "category":self.category.id
    }
    
  def test_create_product(self):
   """teste para verificar a criação de um produto"""
   url = 'api/products/'
   response = self.client.post(url, self.product_data, format = 'json')
   self.assertEqual(response.status_code, status.HTTP_201_CREATED)
   self.assertEqual(Product.objects.count(), 1)
   self.assertEqual(Product.objects.get().name, 'teclado gamer')
   
  def test_list_products(self):
    """Teste para verificar a listagem de Produtos"""
    Product.objects.create(name="Teclado", description="Mecânico", price="200.00", category=self.category)
    url = '/api/products/'
    response = self.client.get(url, format='json')
    self.assertEqual(reponse.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data) > 0)   

# Create your tests here.
