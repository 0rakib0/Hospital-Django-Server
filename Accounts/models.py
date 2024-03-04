from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    user_roll = (
        ('admin','admin'),
        ('doctor','doctor'),
        ('patients','patients'),
    )

    user_type = models.CharField(max_length=20, choices=user_roll, default = 'admin')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
