from django.urls import path
from .views import Todo_Index, Todo_Detail

app_name = 'todo'
urlpatterns = [
    path('', Todo_Index.as_view(), name='index'),
    path('<int:todo_id>/', Todo_Detail.as_view(), name='detail'),
]
