from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend    # django filter 
from rest_framework import filters                               # search and OrderingFilter
from .filters import TodoFilter
from rest_framework.permissions import IsAuthenticated                 # rest_framework_simplejwt security
from rest_framework_simplejwt.authentication import JWTAuthentication  # rest_framework_simplejwt security



class TodoViewset(viewsets.ModelViewSet):     # viewswets for all CRUD in api
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]    # django filter with DjangoFilterBackend, and integration filter with filters.OrderingFilter in custom filter
    # filterset_fields = ['todo', 'Notes','id']       # django filter 
    
    
    # filter_backends = [filters.SearchFilter]        # search
    # search_fields = ['todo', 'Notes','id']          # search
    
    
    # filter_backends = [filters.OrderingFilter]      # OrderingFilter
    # ordering_fields = ['id']                        # OrderingFilter
    
    filterset_class = TodoFilter                      # custom filter should be with line 'filter_backends = [DjangoFilterBackend] '
    ordering_fields = ['id']                          # integration filter with filters.OrderingFilter in custom filter
    
    authentication_classes = [JWTAuthentication]      # rest_framework_simplejwt security
    permission_classes = [IsAuthenticated]            # rest_framework_simplejwt security



