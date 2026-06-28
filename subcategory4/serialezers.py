from rest_framework import serializers
from .models import SubCategory4

class SubCategory4Serializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory4
        fields = '__all__'
