from rest_framework import serializers
from .models import Products4

class Products4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Products4
        fields = '__all__'