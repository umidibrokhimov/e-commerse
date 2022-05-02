from django.db import models

class ProductsCategory(models.Model):
    class Meta():
        verbose_name = 'Product category'
        verbose_name_plural = 'Products categories'
    
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class HomeSlider(models.Model):
    class Meta():
        verbose_name = 'Slide'
        verbose_name_plural = 'Home slides'

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    image = models.ImageField()

class ProductsList(models.Model):
    class Meta():
        verbose_name = 'Product list'
        verbose_name_plural = 'Products lists'
    
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    category = models.OneToOneField(ProductsCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name