from django.views.generic import TemplateView, ListView, DetailView
from .models import *

class Home(ListView):
    template_name = 'index.html'
    queryset = HomeSlider.objects.all()
    context_object_name = 'slides'

class About(TemplateView):
    template_name = 'about.html'

class Products(TemplateView):
    template_name = 'products.html'

class ProductDetail(DetailView):
    template_name = 'product-detail.html'
    queryset = ProductsList.objects.all()
    context_object_name = 'product'

class Contact(TemplateView):
    template_name = 'contact.html'