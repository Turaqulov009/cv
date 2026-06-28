from rest_framework import serializers
from .models import Category2


class Category2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category2
        fields = '__all__'