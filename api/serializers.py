from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    image_url = serializers.SerializerMethodField() 
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 
            'category', 'category_name', 'image', 'image_url'
        ]
        extra_kwargs = {
            'image': {
                'write_only': True,
                'required': False
            }
        }
    
    def get_image_url(self, obj):
        """
        Retorna a URL completa da imagem.
        Funciona tanto com S3 quanto com armazenamento local.
        """
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return Nonem
    
    def to_representation(self, instance):
        """
        Customiza a resposta JSON.
        Remove o campo 'image' (binário) da resposta.
        """
        representation = super().to_representation(instance)
        
        representation.pop('image', None)
        
        return representation
    
    def create(self, validated_data):
        """
        Cria um produto, processando a imagem corretamente.
        """
        image = validated_data.pop('image', None)
        
        product = Product.objects.create(**validated_data)
        
        if image:
            product.image = image
            product.save()
        
        return product
    
    def update(self, instance, validated_data):
        """
        Atualiza um produto, incluindo a imagem.
        """
        image = validated_data.pop('image', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if image is not None:
            instance.image = image
        
        instance.save()
        return instance