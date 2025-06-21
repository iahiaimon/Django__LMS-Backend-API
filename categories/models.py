from django.db import models

from core.models import BaseModel

# Create your models here.

class Category(BaseModel):
    title = models.CharField(max_length=100 , unique = True)