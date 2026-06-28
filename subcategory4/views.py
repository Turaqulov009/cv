from rest_framework import viewsets
from .models import SubCategory4
from .serializers import SubCategory4Serializer

class SubCategory4ViewSet(viewsets.ModelViewSet):
    queryset = SubCategory4.objects.all()
    serializer_class = SubCategory4Serializer