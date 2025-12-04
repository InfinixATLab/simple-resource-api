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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def get_queryset(self):
        return Product.objects.select_related('category').all()
    
    def perform_create(self, serializer):
        instance = serializer.save()
        # Exemplo: log de criação
        print(f"Produto criado: {instance.name} (ID: {instance.id})")
    
    def perform_update(self, serializer):
        instance = serializer.save()
        print(f"Produto atualizado: {instance.name} (ID: {instance.id})")

# Create your views here.