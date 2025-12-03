from django.shortcuts import render
from rest_framework import viewsets
from .models import category, Product
from .serializers import categorySerializer, ProductSerializer

#Use ViewSets para fornercer funcionalidade CRUD completa para Category e Product.
#Configure urls usando DefaultRouter do DRF para registrar os ViewSets.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all().order_by('name')
    serializer_class = categorySerializer

class ProductViewSet(viewsets.ModelVielSet):
    queryset = Product.objects.all().select_related('category').order_by('name')
    serializer_class = ProductSerializer