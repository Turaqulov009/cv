from rest_framework import serializers
from .models import Catigories

class CatigoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catigories
        fields = '__all__'