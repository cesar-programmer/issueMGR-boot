from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Team(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=255)
  
  def __str__(self):
    return self.name

class CustomUser(AbstractUser):
  role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
  team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

