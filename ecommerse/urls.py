from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('products/', Products.as_view(), name='products'),
    path('contact/', Contact.as_view(), name='contact'),
]
