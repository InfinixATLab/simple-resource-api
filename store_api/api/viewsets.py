from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .pagination import ProductPagination
from .exceptions import DuplicateResourceException




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ProductPagination

    # --> Criação de categoria.
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category_name = serializer.validated_data.get('name')

        if category_name:
            existing_category = Category.objects.filter(
                name__iexact=category_name
            ).first()
            
            if existing_category:
                raise DuplicateResourceException(
                    detail=f"Categoria com nome '{category_name}' já existe."
                )
        return super().create(request, *args, **kwargs)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    
    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        product_name = serializer.validated_data.get('name')
        
        
        if product_name:
            existing_product = Product.objects.filter(
                name__iexact=product_name
            ).first()
            
            if existing_product:
                raise DuplicateResourceException(
                    detail=f"Produto com nome '{product_name}' já existe."
                )
        
        return super().create(request, *args, **kwargs)
    
    # Busca produtos pelo nome -> products/search_by_name/?name=notebook
    @action(detail=False, methods=['get'], url_path='search')
    def search_by_name(self, request):
        name = request.query_params.get('name', '')
        products = self.queryset.filter(name__icontains=name)
        
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    