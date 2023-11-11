"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from todo.views import TodoList, TodoDetail, TodoCreate, TodoEdit , TodoDelete
from todo.views import todo_list

urlpatterns = [
    path('admin/', admin.site.urls),
    # CRUD-html
    path('list/',TodoList.as_view()),                  # list
    path('list/<int:pk>',TodoDetail.as_view()),        # detail
    path('list/new',TodoCreate.as_view()),             # create
    path('list/<int:pk>/edit',TodoEdit.as_view()),     # edit
    path('list/<int:pk>/delete',TodoDelete.as_view()), # delet
    
    # CRUD-api-path using router
    path('list/', include('todo.urls')),
    
    # viewjs html
    path('',todo_list)
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)