from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    email_2 = models.EmailField(max_length=255, blank=True)
    bio = models.TextField(blank=True)

    # if the user's still a highschooler, these fields will be blank
    graduation_year = models.IntegerField(default=0000)
    major = models.CharField(max_length=255, blank=True)
    university = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True, blank=True)

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
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.username)
            cnt = 1

            while User.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug = slugify(f"{self.username}-{cnt}")
                cnt += 1

            self.slug = slug

        super().save(*args, **kwargs)

    
# used to store info of unregistered alumni
# only stores info alumni are willing to share
class Alumni(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, blank=True)
    email_2 = models.EmailField(max_length=255, blank=True) # optional
    graduation_year = models.IntegerField(default=0000)
    bio = models.TextField(blank=True) # optional
    slug = models.SlugField(unique=True, blank=True)
    major = models.CharField(max_length=255, blank=True) # optional
    university = models.CharField(max_length=255, blank=True) # optional

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    # generate slug based on name & graduation year
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(f"{self.first_name}-{self.last_name}-{self.graduation_year}")
            cnt = 1

            # ensure slug is unique
            while Alumni.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug = slugify(f"{self.first_name}-{self.last_name}-{self.graduation_year}-{cnt}")
                cnt += 1
                
            self.slug = slug
        
        super().save(*args, **kwargs)