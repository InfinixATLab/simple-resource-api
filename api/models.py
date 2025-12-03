from django.db import models
from decimal import Decimal

# Category(name: CharField)
#Product(name: Charfield, description: TextField, 
#price: DecimalField (2 decimal places), 
#category: ForeignKey(Category, on_delete=models.PROTECT))

class category(models.Model): 
    name = models.CharField(max_length=100, unique=true)

    def__str__(self): return self.name

class Product(models.model):
    name = models.Charfield(max_length=255)
    #descrição do produto sem caracteres máximos
    description = models.TextField(blank=true)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(category, on_delete=models.PROTECT)
    def__str__(self): return self.name
