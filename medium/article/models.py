from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Author(AbstractUser):
  username = models.CharField(blank=True, null=True, max_length=10)
  email = models.EmailField(('email address'), unique=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

  def __str__(self):
    return self.username

class Article(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  body = models.TextField()
  author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)

  def __str__(self):
    return self.title
