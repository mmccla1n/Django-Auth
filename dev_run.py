"""
Passing this file to manage.py will allow print statments put in the views.py to be seen in terminal.
useful for not having to go back top the browsert during initial development
Usage: python manage.py shell < dev_run.py
"""
from users_app.views import AllUsers
from posts_app.views import AllPosts, SinglePostByCategory
from categories_app.views import AllCategories 
from rest_framework.test import APIRequestFactory
from django.core.serializers import serialize

#print(dir(APIRequestFactory()))

"""request = APIRequestFactory().get('/all_users')
print('All Users:\n')
AllUsers.as_view()(request)
new_user = {
        "first_name": "John",
        "last_name": "Smith",
        "email": "bjohn_smith@email.com"
    }"""
#request = APIRequestFactory().post('/all_users', data=new_user, format='json')

#AllUsers.as_view()(request)
"""print()

request = APIRequestFactory().get('/all_posts')
print('All Posts:\n')

AllPosts.as_view()(request)
print()

request = APIRequestFactory().get('/all_categories')
print('All Categories:\n')
AllCategories.as_view()(request)"""

print()
print('Detail view of a specific post in a specific category')
#request = APIRequestFactory().get('http://localhost:8000/api/v1/all_categories/3/posts/4/')

#request = APIRequestFactory().delete('http://localhost:8000/api/v1/all_categories/3/posts/4/')
#SinglePostByCategory.as_view()(request,3,4)
request = APIRequestFactory().post(
    '/api/v1/categories/', 
    {"category": "Test Test Category"}, 
    format='json'
)
AllCategories.as_view()(request)


#ClassSubject.as_view()(request, 'Python')  # Used with classes instance query, 404 response
#Student.as_view()(request, 4)  # Used with students for instance query, 404 error