from django.db import models

# Categories Table
class Categories(models.Model):
    category = models.CharField(max_length=60, blank=False, unique=True, default=None)

    def __str__(self):
        return f'| category: {self.category}'
