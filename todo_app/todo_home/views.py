from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Todo,TodoDone
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.forms.widgets import DateInput


@login_required
def todo_done(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.user.id==todo.author.id:
        tododone = TodoDone(
            title=todo.title,
            description=todo.description,
            due_date=todo.due_date,
            author=request.user,
        )
        tododone.save()
        todo.delete()
    return redirect('todo-home')

def todo_done_list(request):
    # Fetch all the TodoDone objects created by the request.user
    todos = TodoDone.objects.filter(author=request.user)

    # Render the template todo_home/task_done.html with the todos QuerySet as a context variable
    return render(request, 'todo_home/task_done.html', {'todos': todos})


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
