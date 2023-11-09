from django.shortcuts import render
from django.views import generic
from .models import Todo
# Create your views here.

# CRUD-Operations class-based-view


class TodoList(generic.ListView):
    model = Todo
    
    

class TodoDetail(generic.DetailView):
    model = Todo