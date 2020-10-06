from django.db import models

class TodoModel(models.Model):
    task =models.CharField(max_length=20)

# Create your models here.
