from django.db import models
from django.contrib.auth.models import AbstractUser # pridane

# Create your models here.
class CustomUser(AbstractUser): # pridane
    pass