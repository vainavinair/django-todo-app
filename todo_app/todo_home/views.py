from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin


# @login_required(login_url='/user/login/')
# def home(request):
#     user = request.user.id
#     todos = Todo.objects.filter(author=user)
#     context = {'todos': todos}
#     return render(request,'todo_home/todo_list.html',context)

class TaskListView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name="todos"
    def get_queryset(self):
        user = self.request.user.id
        return Todo.objects.filter(author=user)
    
class TaskCreateView(LoginRequiredMixin, CreateView):
    model=Todo
    context_object_name="Task"
    fields=['title','decription','due_date']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model=Todo
    fields=['title','decription','due_date']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)