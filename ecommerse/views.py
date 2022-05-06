from django.views.generic import TemplateView, ListView, DetailView
from .models import *

class Home(ListView):
    template_name = 'index.html'
    queryset = HomeSlider.objects.all()
    context_object_name = 'slides'

class About(ListView):
    template_name = 'about.html'
    queryset = Team.objects.all()
    context_object_name = 'teams'

class Products(ListView):
    template_name = 'products.html'

    def get_queryset(self):
        return HomeSlider.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Products, self).get_context_data(**kwargs)
        context['categories'] = ProductsCategory.objects.all()
        context['products'] = ProductsList.objects.all()
        return context

class ProductDetail(DetailView):
    template_name = 'product-detail.html'
    queryset = ProductsList.objects.all()
    context_object_name = 'product'

class Contact(TemplateView):
    template_name = 'contact.html'