from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    body = models.CharField(max_length=100000000)