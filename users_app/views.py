from rest_framework.views import APIView, Response
from .models import Users
from django.core.serializers import serialize
from .serializers import UsersSerializer
from django.core.exceptions import ValidationError
import json

class AllUsers(APIView):
    def get(self, request):
        """ This method returns all users """
        users = Users.objects.all()  # get all users from table
        # Setting 'many=True' for nested representration
        serialize_users = UsersSerializer(users, many=True)
        #print(dir(serialize_users))
        print(serialize_users.data)
        return Response(serialize_users.data)

    def post(self, request):
        """ This method creates a new user """
        new_user = Users(**request.data)
        
        try:
            new_user.full_clean()
        except ValidationError as err:
            msg = f"ERROR: Unable to create new user | REASON: {err.message_dict}"
            return Response(msg)

        new_user.save()
        serialize_user = UsersSerializer(new_user)
        print(serialize_user.data)
        return Response(serialize_user.data)


class SingleUser(APIView):
    def get(self, request, id):
        """ This method returns a user """
        user = Users.objects.get(pk=id)  # get user by id
        serialize_user = UsersSerializer(user)
        print(serialize_user.data)
        return Response(serialize_user.data)

    def delete(self, request, id):
        """ This method delets a specific post in a specific category """
        user = Users.objects.get(pk=id)  # get user by id  
        name = f'{user.first_name} {user.last_name }'
        user.delete()
        return Response(f'User [{name}], with user_id [{id}] has been removed ')