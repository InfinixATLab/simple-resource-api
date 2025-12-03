from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # O desafio pede 2 casas decimais. max_digits=10 permite preços até 99 milhões.
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    
    # O desafio pede on_delete=models.PROTECT (impede apagar uma categoria se ela tiver produtos)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.name