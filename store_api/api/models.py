from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField()
    description = models.TextField()
    price = models.DecimalField(decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name