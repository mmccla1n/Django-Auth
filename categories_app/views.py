from rest_framework.views import APIView, Response
from .models import Categories
from django.core.serializers import serialize
from .serializers import CategoriesSerializer
#from django.http import Http404
from django.core.exceptions import ValidationError

import json

class AllCategories(APIView):

    def get(self, request):
        """ This method returns all categories """
        categories = Categories.objects.all()  # get all users from table
        # Setting 'many=True' for nested representration
        serialize_categories = CategoriesSerializer(categories, many=True)
        print(serialize_categories.data)
        return Response(serialize_categories.data)
    
    def post(self, request):
        """ This method creates a new category """
        print(request.data)
        #print(**request.data)

        serialize_category = CategoriesSerializer(data=request.data)

        if serialize_category.is_valid():
            print('serialize is valid')
            print(serialize_category.validated_data)
            new_category = serialize_category.save()
            msg = f"The following id [{serialize_category.data['id']}] and catgeory [{serialize_category.data['category']}] is created"
            #return Response(serialize_category.data)
            return Response(msg)
        
        msg = f"Error: Unable to create category [{serialize_category.data['category']}] | "
        msg += f"Error Reason: {serialize_category.errors['category']}"
            
        #return Response(serialize_category.errors)
        return Response(msg)
        
        """new_category = Categories(**request.data)
        new_category.full_clean()
        new_category.save()
        serialize_category = CategoriesSerializer(new_category)
        print(serialize_category.data)
        return Response(serialize_category.data)"""



class SingleCategory(APIView):

    def get_category(self, rcv_id):
        """ THis method retrives by id(Int datatype)"""
        return Categories.objects.get(pk=rcv_id) 


    def get(self, request, id):
        """ This method returns a category """
        #category = Categories.objects.get(pk=id)  # get category by id
        category = self.get_category(id)
        serialize_category = CategoriesSerializer(category)
        print(serialize_category.data)
        return Response(serialize_category.data)

    def put(self, request, id):
        """ This method updates a specific category """
        
        category = self.get_category(id) 
        
        try:
            category.category = request.data['category'] # Update category field
        except KeyError as err:
            msg = f"Error: key {err} missing , unable to update Category. Required key[category]"
            return Response(msg)

        try:
            category.full_clean()  # Check data is correct
            category.save()
            serialize_category = CategoriesSerializer(category)
            msg = f'Updated category for id [{category.id}] to [{category.category}]'
            #return Response(serialize_category.data)
            return Response(msg)
        except ValidationError as err:
            #raise ValidationError(err.message_dict)
            msg = f'ERROR: Unable to apply category [{category.category}]] update | '
            msg += f"REASON: {err.message_dict['category']}"
            return Response(msg)



    def delete(self, request, id):
        """ THis method deltes a specific category by id """
        category = self.get_category(id)
        ctg_name = category.category  # Get category name
        category.delete()
        return Response(f'Category [{ctg_name}] has been removed')
    





        


