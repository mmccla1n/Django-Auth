from django.urls import path, include
from .views import AllPosts

urlpatterns = [
    path('', AllPosts.as_view(), name='all_posts'),
    
]