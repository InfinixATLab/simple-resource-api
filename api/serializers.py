from rest_framework import serializers
from .models import category, Product

#Defina serializers para Category e Product.
#O serializador de Product deve exibir o nome da categoria, não apenas seu ID.

class categorySerializer(serializers.ModelSerializers):
    class Meta:
        model = category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='category', read_only=True)      
    category_id = serializers.PrimaryKeyRelatedField( queryset=Category.objects.all(), source='category', 
        write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'category_id']