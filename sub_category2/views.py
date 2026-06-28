from django.shortcuts import render
from rest_framework import viewsets
from .models import SubCategories
from .serialezers import SubCategoriesSerializer

# Create your views here.

class SubCategory2ViewSet(viewsets.ModelViewSet):
    queryset = SubCategory2.objects.all()
    serializer_class = SubCategory2Serializer