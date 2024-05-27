from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class locations(models.Model):
    name = models.CharField(max_length=40)
    adress = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    comments = models.TextField()
    user_owner = models.ForeignKey(User, on_delete=models.CASCADE,default=0)
