from django.shortcuts import render
from rest_framework import viewsets
from .models import SubCategories
from .serialezers import SubCategoriesSerializer

# Create your views here.

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer