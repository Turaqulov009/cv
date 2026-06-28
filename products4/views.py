from django.shortcuts import render
from rest_framework import viewsets
from .models import Products4
from .serialezers import Products4Serializer

# Create your views here.
class Products4ViewSet(viewsets.ModelViewSet):
    queryset = Products4.objects.all()
    serializer_class = Products4Serializer