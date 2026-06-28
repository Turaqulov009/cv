from rest_framework import serializers
from .models import SubCategory3    


class SubCategory3Serializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory3
        fields = '__all__'