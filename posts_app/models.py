from django.db import models
from users_app.models import Users
from categories_app.models import Categories


# Posts Table
class Posts(models.Model):
    #TODO: Consider what type if any validator should be used for a post ? (Maybe word boundaries or something, maybe)
    post = models.TextField(blank=False, unique=False, default=None)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return f'| post: {self.post} | user_id: {self.user_id} | email: {self.category_id}'