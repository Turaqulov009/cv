from django.shortcuts import render
from rest_framework import viewsets
from .models import Category2
from .serialezers import Category2Serializer

# Create your views here.

class Category2ViewSet(viewsets.ModelViewSet):
    queryset = Category2.objects.all()
    serializer_class = Category2Serializer