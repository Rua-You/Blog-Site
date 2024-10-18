from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)

    # Add unique related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='community_user_set',  # Change this to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='community_user_permissions_set',  # Change this to avoid conflict
        blank=True
    )
    
    def __str__(self):
        return self.email
    
    