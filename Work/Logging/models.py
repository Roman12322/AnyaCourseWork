from django.db import models

from django.db import models

class User(models.Model):
    Login = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=100)

class requests(models.Model):
    sequence = models.CharField(max_length=1000, null=True)
    result = models.CharField(max_length=1000, null=True)
    Username_Id = models.IntegerField(max_length=1000, null=True)