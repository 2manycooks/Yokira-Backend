from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
