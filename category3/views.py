from django.shortcuts import render
from rest_framework import viewsets
from .models import Category3
from .serialezers import Category3Serializer

# Create your views here.
class Category3ViewSet(viewsets.ModelViewSet):
    queryset = Category3.objects.all()
    serializer_class = Category3Serializer
