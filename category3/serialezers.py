from rest_framework import serializers
from .models import Category3

class Category3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category3
        fields = '__all__'