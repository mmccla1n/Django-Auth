from rest_framework import serializers
from .models import Categories

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        #fields = ['id', 'category']
        fields = '__all__'  # Return all fields
