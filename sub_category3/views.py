from django.shortcuts import render
from rest_framework import viewsets
from .models import SubCategories
from .serialezers import SubCategoriesSerializer

# Create your views here.
class SubCategory3ViewSet(viewsets.ModelViewSet):
    queryset = SubCategory3.objects.all()
    serializer_class = SubCategory3Serializer