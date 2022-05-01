from django.db import models

class HomeSlider(models.Model):
    class Meta():
        verbose_name = 'Slide'
        verbose_name_plural = 'Home slides'

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    image = models.ImageField()