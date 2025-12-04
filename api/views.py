from django.shortcuts import render
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import viewsets, parsers


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet para operações CRUD de Categorias.
    Fornece todas as operações padrão: list, create, retrieve, update, destroy.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet para operações CRUD de Produtos.
    Suporta upload de imagens via multipart/form-data.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    
    def get_serializer_context(self):
        """
        Adiciona o request ao contexto do serializer.
        Necessário para o serializer gerar URLs absolutas para as imagens.
        """
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def get_queryset(self):
        """
        Otimiza a query usando select_related para categoria.
        Evita o problema N+1 ao acessar category.name.
        """
        return Product.objects.select_related('category').all()
    
    def perform_create(self, serializer):
        """
        Hook personalizado para criação de produto.
        Pode ser usado para logging ou processamento adicional.
        """
        instance = serializer.save()
        # Exemplo: log de criação
        print(f"Produto criado: {instance.name} (ID: {instance.id})")
    
    def perform_update(self, serializer):
        """
        Hook personalizado para atualização de produto.
        """
        instance = serializer.save()
        print(f"Produto atualizado: {instance.name} (ID: {instance.id})")

# Create your views here.