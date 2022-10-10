from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import UserManager


class User(AbstractUser):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(unique=True,max_length=100,null=True)
    bio = models.TextField(blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]


# Create your models here.
class ApplicationForm(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    roll_number = models.IntegerField(
        help_text="Enter 6 digit roll number",
    )
    password = models.CharField(max_length=100)
    def __str__(self) :
        return self.first_name + "  " + self.last_name
