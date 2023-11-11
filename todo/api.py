from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import viewsets






class TodoViewset(viewsets.ModelViewSet):     # viewswets for all CRUD in api
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer




