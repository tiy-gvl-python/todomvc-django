from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=140)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(null=True)

