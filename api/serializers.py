from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'
    
class ProductSerializer(serializers.MoodelSerializer):
  category_name = serializers.Charfield(source='category_name', read_only=True)
  
  class Meta:
    model = Product
    fields = ['id', 'name', 'description', 'price', 'category', 'category_name']
    read_only_fields = ['category_name']    