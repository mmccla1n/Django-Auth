from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        #fields = ['id', 'first_name', 'last_name', 'email']
        fields = '__all__'  # Return all fields
