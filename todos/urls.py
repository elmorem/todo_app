from django.urls import pathfrom .views import ListTodo, DetailTodo

urlpatterns = [
    path('<int:pk/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
]