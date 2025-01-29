from rest_framework.views import APIView, Response
from .models import Posts
from django.core.serializers import serialize
from .serializers import PostsSerializer
from users_app.models import Users
from categories_app.models import Categories
from django.core.exceptions import ValidationError
#import json

class AllPosts(APIView):
    def get(self, request):
        """ This method returns all posts """
        posts = Posts.objects.all()  # get all users from table
        # Setting 'many=True' for nested representration
        serialize_posts = PostsSerializer(posts, many=True)
        #print(serialize_posts.data)
        return Response(serialize_posts.data)
    
    def post(self, request):
        """ This method creates a new post """
        if 'user_id' in request.data and 'category_id' in request.data:
            user = Users.objects.get(id=request.data['user_id'])
            category = Categories.objects.get(id=request.data['category_id'])

            new_post = Posts(
                post = request.data['post'],
                user_id = user,
                category_id = category
            )

            new_post.full_clean()
            new_post.save()
            serialize_new_post = PostsSerializer(new_post)
            #print(serialize_new_post.data)
        return Response(serialize_new_post.data)
    

class SinglePost(APIView):

    def get_post(self, rcv_id):
        """ THis method retrives by id(Int datatype)"""
        return Posts.objects.get(pk=rcv_id)


    def get(self, request, id):
        """ This method returns a post """
        #category = Categories.objects.get(pk=id)  # get category by id
        post = self.get_post(id)
        serialize_post = PostsSerializer(post)
        #print(serialize_post.data)
        return Response(serialize_post.data)  
    
class AllCategoryPosts(APIView):

    def get(self, request, fk_ctg_id):
        posts = Posts.objects.filter(category_id=fk_ctg_id)
        serialize_posts = PostsSerializer(posts, many=True)
        #print(serialize_posts.data)
        return Response(serialize_posts.data)

    def post(self, request, fk_ctg_id):
        """ This method creates a new post for a given category"""
        
        try:
            user = Users.objects.get(id=request.data['user_id'])
            category = Categories.objects.get(id=request.data['category_id'])
        except KeyError as err:
            msg = f"Error: key(s) are missing {err}, unable to created Post. Required keys are [post, user_id, category_id]"
            return Response(msg)

        new_post = Posts(
            post = request.data['post'],
            user_id = user,
            category_id = category
        )

        new_post.full_clean()
        new_post.save()
        serialize_new_post = PostsSerializer(new_post)
        #print(serialize_new_post.data)
        msg = f"The following id [{serialize_new_post.data['id']}] and post [{serialize_new_post.data['post']}] created"

        return Response(msg)

class SinglePostByCategory(APIView):
    def get(self, request, fk_ctg_id, post_id):
        posts = Posts.objects.filter(category_id=fk_ctg_id, id=post_id )
        serialize_posts = PostsSerializer(posts, many=True)
        print(serialize_posts.data)
        return Response(serialize_posts.data)

    def put(self, request, fk_ctg_id, post_id):
        """ This method updates a specific post in a specific category """
        posts = SinglePost().get_post(post_id)  # Get post object

        try:
            posts.post = request.data['post']  # Update post field
        except KeyError as err:
            msg = f"Error: key {err} missing , unable to update Category. Required key[post]"
            return Response(msg)
        
        posts.full_clean()
        posts.save()
        serialize_posts = PostsSerializer(posts)
        msg = f"Updated post for id [{post_id}] to [{posts.post}]"
        return Response(msg)
    
    def delete(self, request, fk_ctg_id, post_id):
        """ This method delets a specific post in a specific category"""
        posts = SinglePost().get_post(post_id)  # Get post object
        category = Categories.objects.get(id=fk_ctg_id)
        post = posts.post
        #print(PostsSerializer(post), category.category)        
        posts.delete()
        return Response(f'post [{post}] belonging to category [{category.category}]has been removed ')
    

