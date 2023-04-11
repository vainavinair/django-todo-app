from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(default=date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=User.objects.first().id)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo-home')

class TodoDone(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(default=date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=User.objects.first().id)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('todo-home')