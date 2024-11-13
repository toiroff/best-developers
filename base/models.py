from django.db import models

# Create your models here.
class Advocate(models.Model):
  username = models.CharField(max_length=200)
  bio = models.TextField(null=True,blank=True)

  def __str__(self):
    return self.username
  