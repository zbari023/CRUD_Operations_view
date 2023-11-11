from django.db import models
from django.utils import timezone
# Create your models here.



class Todo(models.Model):
    todo = models.TextField(max_length=2000)
    Notes= models.TextField(max_length=2000)
    Action = models.TextField(max_length=2000)
    def __str__(self):
        return self.todo
    