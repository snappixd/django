from django.urls import path, include
from .views import index, about_product

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>', about_product, name='about_product'),
]
