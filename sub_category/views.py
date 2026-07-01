from django.shortcuts import render
from rest_framework import viewsets
from .models import SubCategory
from .serializers import SubCategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer