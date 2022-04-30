from django.contrib import admin
from django.urls import path
from ecommerse.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home),
]
