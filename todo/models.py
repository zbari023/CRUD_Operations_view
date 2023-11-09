from django.db import models
from django.utils import timezone
# Create your models here.

STATUS = (
    ('notstarted', 'notstarted'),
    ('inprogress', 'inprogress'),
    ('completed', 'completed'),
)

class Todo(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    status = models.CharField(max_length=20,choices=STATUS)
    created_datum = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    