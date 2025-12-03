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

class CategoryViewSet(viewsets.ModelViewSet):
    """Fornece CRUD para categorias."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema_view(
    create=extend_schema(
        summary="Cria um novo produto",
        description="Endpoint para criar produtos com upload de imagem.",
        request=PRODUCT_UPLOAD_SCHEMA
    )
)
class ProductViewSet(viewsets.ModelViewSet):
    """Fornece CRUD para produtos."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)