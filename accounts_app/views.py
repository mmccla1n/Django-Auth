
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import SignUpSerializer
from rest_framework.permissions import AllowAny

class UserSignUp(CreateAPIView):
    users = User.objects.all()
    #class_serializer = SignUpSerializer
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

    #def create_user(self, serilized_data):
    def perform_create(self, serilized_data):

        # Check if serilized_data is valid
        if serilized_data.is_valid():
            user_name = serilized_data.validated_data['username']
            pw = serilized_data.validated_data['password']
            User.objects.create_user(username=user_name, password=pw)

