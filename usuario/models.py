from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuario(AbstractUser):
    phone = models.CharField(max_length=18, null=False)
    def __str__(self):
        return self.username