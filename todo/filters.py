
# custom filter

from django_filters import rest_framework as filter
from .models import Todo



class TodoFilter(filter.FilterSet):
    class Meta:
        model = Todo
        fields = {
            'id' : ['range','lte','gte'],   # lte is less than or equal to , gte is greater than or equal to
            'todo' : ['contains'],
            'Notes': ['contains']
        }