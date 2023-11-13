
# custom filter

from django_filters import rest_framework as filter
from .models import Todo



class TodoFilter(filter.FilterSet):
    class Meta:
        model = Todo
        fields = {
            'id' : ['range'],
            'todo' : ['contains'],
            'Notes': ['contains']
        }