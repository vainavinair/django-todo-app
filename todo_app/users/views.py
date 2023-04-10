from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserReg

def register(request):
    
    if request.method=="POST":
        form = UserReg(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome to Todo-App {username}')
            return redirect('todo-home')
    
    form = UserReg()
    return render(request,'users/register.html',{'form':form})
