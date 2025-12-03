from django.contrib import admin
from .models import Category, Product

# Cria o nome do produto e a categoria na listagem do admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#Cria o nome do produto, preço e categoria na listagem do admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
