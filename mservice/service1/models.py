from django.db import models

# Create your models here.

class Service1(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    
