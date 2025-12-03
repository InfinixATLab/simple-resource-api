from rest_framework.test import APITestCase
from django.urls import reverse

from api.models import Category, Product

class CategoryAPITests(APITestCase):
    def setUp(self):
        # Cria uma categoria para usar nos testes
        self.category = Category.objects.create(name="Roupas")

        # Define as URLs para os endpoints da API
        self.list_url = reverse('category-list')
        self.detail_url = reverse('category-detail', args=[self.category.id])

    def test_create_category_success(self):
        data = {"name": "Eletrônicos"}
        response = self.client.post(self.list_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], "Eletrônicos")

    def test_create_category_failure(self):
        data = {"name": ""}  # Nome vazio deve falhar
        response = self.client.post(self.list_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_retrieve_category(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], "Roupas")

    def test_retrieve_category_not_found(self):
        not_found_url = reverse('category-detail', args=[999])
        response = self.client.get(not_found_url)
        self.assertEqual(response.status_code, 404)

    def test_update_category_success(self):
        data = {"name": "Eletrônicos"}
        response = self.client.put(self.detail_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], "Eletrônicos")

    def test_update_category_failure(self):
        data = {"name": ""}  # Nome vazio deve falhar
        response = self.client.put(self.detail_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete_category_success(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)

    def test_delete_category_not_found(self):
        not_found_url = reverse('category-detail', args=[999])
        response = self.client.delete(not_found_url)
        self.assertEqual(response.status_code, 404)

    def test_list_categories(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], "Roupas")

    def test_list_categories_multiple(self):
        Category.objects.create(name="Eletrônicos")
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_list_categories_empty(self):
        Category.objects.all().delete()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)

class ProductAPITests(APITestCase):
    def setUp(self):
        # Cria uma categoria para associar aos produtos
        self.category = Category.objects.create(name="Roupas")

        # Cria o produto para usar nos testes
        self.product = Product.objects.create(
            name="Camiseta",
            description="Camiseta de algodão",
            price=29.99,
            category=self.category
        )

        # Define as URLs para os endpoints da API
        self.list_url = reverse('product-list')
        self.detail_url = reverse('product-detail', args=[self.product.id])

    def test_create_product_success(self):
        data = {
            "name": "Calça Jeans",
            "description": "Calça jeans azul",
            "price": 99.99,
            "category_id": self.category.id
        }
        response = self.client.post(self.list_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], "Calça Jeans")

    def test_create_product_failure(self):
        data = {
            "name": "",
            "description": "Descrição inválida",
            "price": -10,
            "category_id": 999  
        }
        response = self.client.post(self.list_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_retrieve_product(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], "Camiseta")

    def test_retrieve_product_not_found(self):
        not_found_url = reverse('product-detail', args=[999])
        response = self.client.get(not_found_url)
        self.assertEqual(response.status_code, 404)

    def test_update_product_success(self):
        data = {
            "name": "Camiseta Atualizada",
            "description": "Descrição atualizada",
            "price": 39.99,
            "category_id": self.category.id
        }
        response = self.client.put(self.detail_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], "Camiseta Atualizada")

    def test_update_product_failure(self):
        data = {
            "name": "",
            "description": "Descrição inválida",
            "price": -20,
            "category_id": 999  
        }
        response = self.client.put(self.detail_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_patch_product_success(self):
        data = {
            "price": 49.99
        }
        response = self.client.patch(self.detail_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(response.json()['price']), 49.99)

    def test_patch_product_failure(self):
        data = {
            "price": -30  # Preço negativo deve falhar
        }
        response = self.client.patch(self.detail_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_delete_product_success(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)

    def test_delete_product_not_found(self):
        not_found_url = reverse('product-detail', args=[999])
        response = self.client.delete(not_found_url)
        self.assertEqual(response.status_code, 404)

    def test_list_products(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], "Camiseta")

    def test_list_products_multiple(self):
        Product.objects.create(
            name="Calça Jeans",
            description="Calça jeans azul",
            price=99.99,
            category=self.category
        )
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_list_products_empty(self):
        Product.objects.all().delete()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)

    def test_product_category_name_in_response(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['category'], "Roupas")