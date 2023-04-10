from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    decription = models.TextField()
    due_date = models.DateField(default=date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=User.objects.first().id)