from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# Configuração swagger para upload de arquivos
PRODUCT_UPLOAD_SCHEMA = {
    'multipart/form-data': {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'description': {'type': 'string'},
            'price': {'type': 'number'},
            'category': {'type': 'integer'},
            'image': {'type': 'string', 'format': 'binary'},
        },
        'required': ['name', 'description', 'price', 'category']
    }
}

@extend_schema_view(
    list=extend_schema(
        summary="Listar Categorias",
        description="Retorna uma lista de todas as categorias disponíveis no sistema."
    ),    
    create=extend_schema(
        summary="Criar nova Categoria",
        description="Cadastra uma nova categoria no banco de dados."
    ),
    retrieve=extend_schema(
        summary="Detalhar Categoria",
        description="Retorna os dados de uma categoria específica pelo ID."
    ),
    update=extend_schema(summary="Atualizar Categoria"),
    partial_update=extend_schema(summary="Atualizar Categoria parcialmente"),
    destroy=extend_schema(
        summary="Excluir Categoria",
        description="Remove uma categoria definitivamente. Não pode remover se houver produtos vinculados."
    )
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


@extend_schema_view(
    create=extend_schema(
        summary="Cria um novo produto",
        description="Endpoint para criar produtos com upload de imagem.",
        request=PRODUCT_UPLOAD_SCHEMA
    ),
    list=extend_schema(
        summary="Listar Produtos",
        description="Retorna uma lista de todos os produtos disponíveis no sistema."
    ),    
    retrieve=extend_schema(
        summary="Detalhar Produtos",
        description="Retorna os dados de um produto específico pelo ID."
    ),
    update=extend_schema(summary="Atualizar produto"),
    partial_update=extend_schema(summary="Atualizar produto parcialmente"),
    destroy=extend_schema(
        summary="Excluir produto",
        description="Remove um produto definitivamente. "
    )
)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)