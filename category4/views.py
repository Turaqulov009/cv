from django.shortcuts import render
from rest_framework import viewsets
from .models import Category4
from .serialezers import Category4Serializer

# Create your views here.
class Category4ViewSet(viewsets.ModelViewSet):
    queryset = Category4.objects.all()
    serializer_class = Category4Serializer