from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend    # django filter search





class TodoViewset(viewsets.ModelViewSet):     # viewswets for all CRUD in api
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend]         # django filter search
    filterset_fields = ['todo', 'Notes']            # django filter search



