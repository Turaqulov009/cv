from rest_framework import viewsets
from .models import SubCategories
from .serialezers import SubCategoriesSerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer