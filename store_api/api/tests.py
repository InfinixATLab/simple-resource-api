from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Product

class ProductTests(APITestCase):
    
    def setUp(self): 
        
       
        self.category = Category.objects.create(name="Eletrodomésticos")
        
        # URL da listagem de produtos
        self.list_url = reverse('product-list') 

    def test_create_product(self):
        """
        Teste 1: Verifica se conseguimos criar um Produto via API
        """
        data = {
            "name": "Geladeira",
            "description": "Duplex Frost Free",
            "price": "2500.00",
            "category": self.category.id  # Enviamos o ID da categoria
        }
        
        # Fazemos um POST (simulando o envio de formulário)
        response = self.client.post(self.list_url, data, format='json')
        
        # Verificamos se deu sucesso (Código 201 Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Verificamos se o produto foi salvo no banco
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Geladeira')

    def test_list_products(self):
        """
        Teste 2: Verifica se a listagem de produtos funciona e traz os dados certos
        """
        # Criamos um produto direto no banco
        Product.objects.create(
            name="Microondas", 
            description="30 Litros", 
            price="400.00", 
            category=self.category
        )
        
        
        response = self.client.get(self.list_url)
        
    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['category_name'], 'Eletrodomésticos')
