from django.db import models

# Create your models here.

class Pages(models.Model):
    name = models.TextField()
    page = models.TextField()
