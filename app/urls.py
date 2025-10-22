from django.contrib import admin
from django.urls import path
from todolist.views import TodosListView, TodoNewCreateView, TodoDetailView, TodoUpdateView, TodoDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', TodosListView.as_view(), name='todos_list'),
    path('new_todo/', TodoNewCreateView.as_view(), name='new_todo'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
]
