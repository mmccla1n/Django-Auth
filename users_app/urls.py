
from django.urls import path, include
from .views import AllUsers, SingleUser

urlpatterns = [
    path('', AllUsers.as_view(), name='all_users'),
    path('<int:id>/', SingleUser.as_view(), name='single_category')
    
]
