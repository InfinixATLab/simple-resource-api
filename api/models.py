from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # 2 casas decimais:
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # não vai deixar apagar uma categoria se ela tiver produtos
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name