from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serialezers import ProductSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer