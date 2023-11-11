from django.urls import path, include
from .api import TodoViewset
from rest_framework.routers import DefaultRouter ### 




router = DefaultRouter()
router.register('',TodoViewset)

urlpatterns = [
    path('api/', include(router.urls))
]


