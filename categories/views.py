from rest_framework import viewsets
from .models import Catigories
from .serializers import CatigoriesSerializer

# Create your views here.

class CatigoriesViewSet(viewsets.ModelViewSet):
    queryset = Catigories.objects.all()
    serializer_class = CatigoriesSerializer
