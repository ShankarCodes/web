from django.contrib import admin
from django.contrib.auth.models import User
from .models import ExerciseData
from .models import Field

admin.site.register(ExerciseData)
admin.site.register(Field)

# Register your models here.
