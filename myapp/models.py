from django.db import models

# Create your models here.
class MyTable(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()

