from django.db import models

class Category(models.Model):
  name = models.Charfiel(max_length=255)
  
  def __str__(self):
      return self.name
  
  class Meta:
    verbose_name_plural = "Categories"  


class Product(models.Model):
  name = models.Charfiel(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
  image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="imagem do Produto")
  
  def __str__(self):
      return self.name
  
# Create your models here.
