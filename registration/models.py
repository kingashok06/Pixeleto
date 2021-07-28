from django.db import models
from django.contrib .auth.models import User
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
