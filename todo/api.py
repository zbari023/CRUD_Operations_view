from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo




class TodoListAPI(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    


class TodoDetailAPI(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer