from django.db import models
from core.models.base_model import BaseModel
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        STUDENTS = "s" , "Student"
        TEACHERS = "t" , "Teacher"
        ADMIN = "a" , "Admin"
    mobile = models.CharField(max_length=15, unique=True)
    role = models.CharField(
        max_length=20,
        choices = RoleChoices.choices,
        default = RoleChoices.STUDENTS

    )
