###############################################################################
# FILE     : views.py
# SYNOPSIS : All Django views for the app model are here.
# LICENSE  : MIT
###############################################################################


###############################################################################
# IMPORTS
###############################################################################

import requests

from django.http import JsonResponse
from django.shortcuts import (
    HttpResponseRedirect,
    get_object_or_404,
    render,
)
from django.urls import reverse

from .forms import (
    TodoFormCreate,
    TodoFormUpdate,
)
from .models import Todo
from .weather import (
    API_KEY,
    BASE_URL_WEATHER,
    ZERO_C_IN_K,
)


###############################################################################
# FUNCTIONS
###############################################################################

def index(request):
    """Provides the list view of all tasks."""

    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})


def show(request, todo_id):
    """Provides a detail view of an individual task."""

    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, 'todos/show.html', {'todo': todo})


def create(request):
    """Provides the form for the creation of a new task."""

    form = TodoFormCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('todos:index'))

    return render(request, 'todos/create.html', {'form': form})


def update(request, todo_id):
    """Provides the form for updating an existing task."""

    todo = get_object_or_404(Todo, id=todo_id)
    form = TodoFormUpdate(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('todos:index'))

    return render(request, 'todos/update.html', {'form': form, 'todo': todo})


def delete(request, todo_id):
    """Provides the form for the deletion of an existing task."""

    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return HttpResponseRedirect(reverse('todos:index'))

    return render(request, 'todos/delete.html', {'todo': todo})


def weather(request):
    """Returns JSON for integer temperature in Celsius at a location."""

    location = request.GET.get('q', None)
    if location:
        url_weather = (
            f"{BASE_URL_WEATHER}appid={API_KEY}&q={location}"
        )
        response = requests.get(url_weather)
        response_json = response.json()
        if response_json['cod'] != '404':
            main_info = response_json['main']
            current_temperature = float(main_info['temp']) - ZERO_C_IN_K
            return JsonResponse(
                {'temperature': f"{round(current_temperature)}"}
            )


###############################################################################
# END
###############################################################################
# Local variables:
# mode: python
# End:
