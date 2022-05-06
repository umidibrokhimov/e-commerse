from django.db import models

class ProductsCategory(models.Model):
    class Meta():
        verbose_name = 'Product category'
        verbose_name_plural = 'Products categories'
    
    name = models.CharField(max_length=20)
    asd = models.CharField(max_length=12)

    def __str__(self):
        return self.asd

class HomeSlider(models.Model):
    class Meta():
        verbose_name = 'Slide'
        verbose_name_plural = 'Home slides'

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.name

class ProductsList(models.Model):
    class Meta():
        verbose_name = 'Product list'
        verbose_name_plural = 'Products lists'
    
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    category = models.OneToOneField(ProductsCategory, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.name

class Team(models.Model):
    class Meta():
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    fullname = models.CharField(max_length=50)
    job = models.CharField(max_length=20)
    about = models.TextField()
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    behance_link = models.URLField(blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.fullname