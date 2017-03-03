from django.db import models

# Create your models here.

class channel(models.Model):
    name=models.CharField(max_length=100)
    source=models.CharField(max_length=200)
    id=models.IntegerField(primary_key=True)