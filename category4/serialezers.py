from rest_framework import serializers
from .models import Category4

class Category4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category4
        fields = '__all__'