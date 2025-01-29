from rest_framework import serializers
from .models import Posts

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        #fields = ['id', 'first_name', 'last_name', 'email']
        fields = '__all__'  # Return all fields
