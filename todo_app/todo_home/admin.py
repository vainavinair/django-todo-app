from django.contrib import admin
from .models import Todo,TodoDone

# Register your models here.
admin.site.register(Todo)
admin.site.register(TodoDone)