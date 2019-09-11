from django.urls import path, include
from . import views

app_name= 'home'
urlpatterns = [
    # path('', views.Poll_View.as_view(), name ='home_index'),
    path('', views.index, name ='home_index'),
]
