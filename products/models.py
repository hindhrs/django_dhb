from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  image_name = models.CharField(max_length=255)
  sizes = models.CharField(max_length=255) 
  category = models.CharField(max_length=255)  

  def __str__(self):
    return (f"{self.category}-{self.name}")
  def img_path(self):
    return (f"images/products/{self.image_name}")
  def get_sizes(self):
    return self.sizes.split(" ")
    
class Category(models.Model):
  name = models.CharField(max_length=30)
  image_name=models.CharField(max_length=30)
  def __str__(self):
    return self.name
  def img_path(self):
    return (f"images/logos/{self.image_name}")
  class Meta:
        verbose_name_plural = "Categories"



 
