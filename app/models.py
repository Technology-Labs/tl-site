from django.db import models

# Create your models here.

class Leads(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    description = models.TextField()
    budget = models.IntegerField(default=0)