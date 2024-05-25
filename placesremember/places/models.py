from django.db import models

# Create your models here.
class tablica(models.Model):
    title = models.CharField(max_length=100)