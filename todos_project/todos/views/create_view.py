###############################################################################
# FILE     : create_view.py
# SYNOPSIS : The Django 3 class-view for creating new objects is here.
# LICENSE  : MIT
###############################################################################


###############################################################################
# IMPORTS
###############################################################################

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from todos.forms import TodoFormCreate
from todos.models import Todo


###############################################################################
# CLASSES
###############################################################################

class TodoCreateView(CreateView):
    """Class-based view of a form to create a new task."""

    model = Todo
    form_class = TodoFormCreate
    template_name = 'todos/todo_create_view.html'
    success_url = reverse_lazy('todos:list')


###############################################################################
# END
###############################################################################
# Local variables:
# mode: python
# End:
