from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/user/login/')
def home(request):
    return render(request,'todo_home/home.html')
