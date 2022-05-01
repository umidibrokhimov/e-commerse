from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'index.html'

class About(TemplateView):
    template_name = 'about.html'

class Products(TemplateView):
    template_name = 'products.html'

class Contact(TemplateView):
    template_name = 'contact.html'