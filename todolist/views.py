from todolist.models import Todo
from todolist.forms import TodoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class TodosListView(ListView):
  model = Todo
  template_name = 'todos.html'
  context_object_name = 'todos'

  def get_queryset(self):
    todos = super().get_queryset().order_by('task')
    search = self.request.GET.get('search')
    if search:
      todos = todos.filter(task__icontains=search)
    return todos

class TodoDetailView(DetailView):
  model = Todo
  template_name = 'todo_detail.html'

class TodoNewCreateView(CreateView):
  model = Todo
  form_class = TodoForm
  template_name = 'new_todo.html'
  success_url = '/todos/'

class TodoUpdateView(UpdateView):
  model = Todo
  form_class = TodoForm
  template_name = 'todo_update.html'
  
  def get_success_url(self):
    return reverse_lazy('todo_detail', kwargs={'pk': self.object.pk})
  
class TodoDeleteView(DeleteView):
  model = Todo
  template_name = 'todo_delete.html'
  success_url = '/todos/'