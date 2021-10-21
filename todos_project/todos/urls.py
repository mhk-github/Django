from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:todo_id>/', views.show, name='show'),
    path('<int:todo_id>/update', views.update, name='update'),
    path('<int:todo_id>/delete', views.delete, name='delete'),
    path('weather/', views.weather, name='weather'),
]
