from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Category, Product

class ProductAPITestCase(APITestCase):

    def setUp(self):
        # Criamos uma categoria para usar nos testes
        self.category = Category.objects.create(name="Eletrônicos")

        # URL para criar e listar produtos via router do DRF
        self.product_list_url = reverse("product-list")

    def test_create_product(self):
        """
        Testa se um produto é criado corretamente com POST.
        """
        data = {
            "name": "Mouse Gamer",
            "price": "199.90",
            "category": self.category.id
        }

        response = self.client.post(self.product_list_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.first().name, "Mouse Gamer")

    def test_list_products(self):
        """
        Testa se a listagem de produtos retorna os itens corretamente.
        """
        Product.objects.create(
            name="Teclado Mecânico",
            price="399.90",
            category=self.category
        )

        response = self.client.get(self.product_list_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Teclado Mecânico")