from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.forms.widgets import DateInput


class TaskListView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name="todos"
    def get_queryset(self):
        user = self.request.user.id
        return Todo.objects.filter(author=user)
    
class TaskCreateView(LoginRequiredMixin, CreateView):
    model=Todo
    context_object_name="Task"
    fields=['title','description','due_date']

    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['due_date'].widget = DateInput(attrs={'type': 'date', 'placeholder':'enter the due date'}, format='%Y-%m-%d')
        form.fields['title'].widget.attrs.update({'placeholder': 'Enter the title of Task'})
        form.fields['description'].widget.attrs.update({'placeholder': 'Enter the description of Task'})
        return form

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Todo
    fields=['title','description','due_date']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['due_date'].widget = DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        return form

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        task= self.get_object()
        if self.request.user==task.author:
            return True
        return False

    
class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model= Todo
    success_url='/'
    def test_func(self):
        task= self.get_object()
        if self.request.user==task.author:
            return True
        return False
