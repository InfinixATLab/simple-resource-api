from django.contrib import admin
from .models import Category, Product 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Mostra id e nome

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category') # Mostra essas colunas
    list_filter = ('category',) # Cria filtro por categoria
    search_fields = ('name',)   # Cria barra de busca por nome