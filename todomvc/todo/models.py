from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=140, blank=False)
    completed = models.BooleanField()
    order = models.IntegerField(null=True)