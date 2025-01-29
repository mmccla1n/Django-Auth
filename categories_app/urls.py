from django.urls import path, include
from .views import AllCategories, SingleCategory
from posts_app.views import AllCategoryPosts, SinglePostByCategory

urlpatterns = [
    path('', AllCategories.as_view(), name='all_categories'),
    path('<int:id>/', SingleCategory.as_view(), name='single_category'),
    path('<int:fk_ctg_id>/posts', AllCategoryPosts.as_view(), name='category_posts'),
    path('<int:fk_ctg_id>/posts/<int:post_id>', SinglePostByCategory.as_view(), name='specific_post_and_category')
    
]