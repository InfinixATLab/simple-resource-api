from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    # aceita category como ID no POST/PUT/PATCH
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # description opcional para permitir POSTs sem o campo
    description = serializers.CharField(required=False, allow_blank=True)
    # mostra o nome da categoria na saída, somente leitura
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "category", "category_name"]