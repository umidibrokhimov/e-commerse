from django.urls import path
from .views import *

app_name = 'ecommerse'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('products/', Products.as_view(), name='products'),
    path('contact/', Contact.as_view(), name='contact'),
    path('products/<int:pk>detail/', ProductDetail.as_view(), name='product-detail'),
]
