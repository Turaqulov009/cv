from rest_framework import serializers
from .models import Product3

class Product3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product3
        fields = '__all__'