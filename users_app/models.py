from django.db import models
from .validators import validate_name_format, validate_email


# Users Table
class Users(models.Model):
    first_name = models.CharField(max_length=60, blank=False, unique=False, default=None, validators=[validate_name_format])
    last_name = models.CharField(max_length=60, blank=False, unique=False, default=None, validators=[validate_name_format])
    email = models.CharField(max_length=100, blank=False, unique=True, validators=[validate_email])

    def __str__(self):
        return f'| first_name: {self.first_name} | last_name: {self.last_name} | email: {self.email}'