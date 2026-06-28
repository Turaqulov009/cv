from rest_framework import serializers
from .models import SubCategory2

class SubCategory2Serializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory2
        fields = '__all__'