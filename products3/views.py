from django.shortcuts import render
from rest_framework import viewsets
from .models import Product2
from .serialezers import Product2Serializer
# Create your views here.
class Product3ViewSet(viewsets.ModelViewSet):
    queryset = Product3.objects.all()
    serializer_class = Product3Serializer