from rest_framework import serializers
from .models import SubCategories

class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = '__all__'