from django.db import models

class Detail(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    phone = models.CharField(max_length=15)
    
