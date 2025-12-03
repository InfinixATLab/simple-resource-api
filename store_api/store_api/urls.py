from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CategoryViewSet, ProductViewSet

# Criação do Roteador (Gerencia as URLs automaticamente)
router = DefaultRouter()

# O 'basename' é o apelido que o teste usa para encontrar a rota.
# Se basename='product', o Django cria internamente o nome 'product-list'.
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluimos as rotas do roteador aqui com o prefixo 'api/'
    path('api/', include(router.urls)),
]