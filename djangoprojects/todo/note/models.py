from django.db import models
from django.utils import timezone
# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    
    