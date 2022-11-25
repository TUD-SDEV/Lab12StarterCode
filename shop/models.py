from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.TextField()  

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('product_list_by_category',args=[self.id])


class Product(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to='product_images', blank=True)
    category = models.ForeignKey(Category, related_name = 'products', on_delete=models.CASCADE)
    description = models.TextField()
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
