###############################################################################
# FILE     : urls.py
# SYNOPSIS : All URLs specific to this app are stated here.
# LICENSE  : MIT
###############################################################################


###############################################################################
# IMPORTS
###############################################################################

from django.urls import path

from . import views


###############################################################################
# URLS
###############################################################################

app_name = 'todos'
urlpatterns = [
    path('', views.TodoListView.as_view(), name='list'),
    path('create/', views.TodoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.TodoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.TodoDeleteView.as_view(), name='delete'),
    path('weather/', views.WeatherView.as_view(), name='weather'),
]


###############################################################################
# END
###############################################################################
# Local variables:
# mode: python
# End:
