from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=20, unique=True)
    fingerprint = models.ImageField(null = True)