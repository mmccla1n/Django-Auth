
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserSignUp

urlpatterns = [
    path('get-token', obtain_auth_token ),
    path('signup', UserSignUp.as_view())
    
]
