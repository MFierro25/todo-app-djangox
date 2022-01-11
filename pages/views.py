from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import TodoItem
from django.urls import reverse_lazy

    
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class TodoListView(ListView):
    template_name = 'pages/todo_list.html'
    model = TodoItem
    
class TodoCreateView(CreateView):
    template_name = 'pages/todo_create.html'
    model = TodoItem 
    fields = ['content', 'date_created']

class TodoUpdateView(UpdateView):
    template_name = 'pages/todo_update.html'
    model = TodoItem
    fields = ['content', 'date_created']

class TodoDeleteView(DeleteView):
    template_name = 'pages/todo_delete.html'
    model = TodoItem
    success_url = reverse_lazy("todo_list")
    
class TodoDetailView(DetailView):
    template_name = 'pages/todo_detail.html'
    model = TodoItem