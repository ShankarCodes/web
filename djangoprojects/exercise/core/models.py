from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Field(models.Model):
    label = models.CharField(max_length=100)
    content = models.CharField(max_length=500)

class ExerciseData(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="owner")
    field1 = models.ForeignKey(Field,on_delete=models.CASCADE,related_name="field1")
    field2 = models.ForeignKey(Field,on_delete=models.CASCADE,related_name="field2")
    field3 = models.ForeignKey(Field,on_delete=models.CASCADE,related_name="field3")

