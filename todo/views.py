from django.shortcuts import render
from django.views import generic  # *********here***********
from .models import Todo
# Create your views here.

# CRUD-Operations class-based-view


class TodoList(generic.ListView):    # list view
    model = Todo
    
    

class TodoDetail(generic.DetailView):  # detail view
    model = Todo
    
class TodoCreate(generic.CreateView):  # creating view
    model = Todo
    fields = '__all__'
    success_url = '/list/'
    
    
class TodoEdit(generic.UpdateView):  # Editing the created post
    model = Todo
    fields = '__all__'
    success_url = '/list/'
    template_name = 'todo/edit.html'
    
class TodoDelete(generic.DeleteView): # Delete the created post
    model = Todo
    success_url = '/list/'