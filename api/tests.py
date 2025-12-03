import io
from PIL import Image
from rest_framework.test import APITestCase 
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Category, Product

class ProductAPITestCase(APITestCase):
    """Suite de testes completo para operações de CRUD de Produtos."""
    
    def setUp(self):
        """Configuração inicial executada antes de CADA teste. Cria uma categoria base e define as URLs principais."""
        self.category = Category.objects.create(name="Eletrônicos")

    def _generate_image_file(self):
        """Método para gerar imagem."""
        file = io.BytesIO()
        image = Image.new('RGB', (100, 100), 'red')
        image.save(file, 'jpeg')
        file.seek(0)
        return SimpleUploadedFile("teste.jpg", file.read(), content_type="image/jpeg")

    def test_create_product(self):
        """Objetivo: Verificar se a API aceita multipart/form-data com imagem."""
      
        # Praparando dados
        payload = {
            "name": "Celular X",
            "description": "Um celular de teste",
            "price": "1500.00",
            "category": self.category.id, 
            "image": self._generate_image_file()
        }
        
        response = self.client.post('/api/products/', payload, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Validações
        self.assertEqual(Product.objects.count(), 1)
        created_product = Product.objects.get()
        self.assertEqual(created_product.name, "Celular X")
        self.assertTrue(created_product.image)

    def test_list_products(self):
        """Objetivo: Listar produtos e garantir que a resposta traga o nome da categoria."""
     
        # Preparando dados
        Product.objects.create(
            name="Teclado", 
            description="Mecânico", 
            price="200.00", 
            category=self.category
        )

        response = self.client.get('/api/products/')

        # Validações
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['count'], 1) 
        product_data = response.data['results'][0]
        
        self.assertIn('category_name', product_data)
        self.assertEqual(product_data['category_name'], "Eletrônicos")

    def test_retrieve_product_detail(self):
        """Objetivo: Verificar se o endpoint de detalhe funciona e traz o nome da categoria."""

        # Preparando dados
        product = Product.objects.create(
            name="Teclado", 
            description="Mecânico", 
            price="200.00", 
            category=self.category 
        )

        url = f'/api/products/{product.id}/'
        response = self.client.get(url)

        # Validações
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Teclado")
        self.assertEqual(response.data['category_name'], "Eletrônicos")

    def test_update_product_price(self):
        """Objetivo: Mudar apenas o preço de um produto existente."""
       
        # Preparando dados
        product = Product.objects.create(
            name="Teclado", 
            description="Mecânico", 
            price="200.00", 
            category=self.category
        )

        url = f'/api/products/{product.id}/'

        # Executa o PATCH
        new_data = {"price": "350.00"}
        response = self.client.patch(url, new_data)

        # Validações
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product.refresh_from_db() 
        self.assertEqual(product.price, 350.00)
        self.assertEqual(product.name, "Teclado")

    def test_delete_product(self):
        """Objetivo: Garantir que o produto suma do banco."""
        
        # Preparando dados
        product = Product.objects.create(
            name="Teclado", 
            description="Mecânico", 
            price="200.00", 
            category=self.category
        )

        url = f'/api/products/{product.id}/'

        response = self.client.delete(url)

        # Validações
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)