from django.urls import path
from .views import TodoCompletedList, TodoListCreate, TodoUpdateDelete, TodoComplete, signup


app_name = 'api'

urlpatterns = [
    path('todos', TodoListCreate.as_view()),
    path('todos/<int:pk>', TodoUpdateDelete.as_view()),
    path('todos/<int:pk>/complete', TodoComplete.as_view()),
    path('todos/completed', TodoCompletedList.as_view()),

    path('signup', signup),
]
