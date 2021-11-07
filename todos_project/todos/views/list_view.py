###############################################################################
# FILE     : list_view.py
# SYNOPSIS : The Django 3 class-view to show all existing objects is here.
# LICENSE  : MIT
###############################################################################


###############################################################################
# IMPORTS
###############################################################################

from django.views.generic import ListView

from todos.models import Todo


###############################################################################
# CLASSES
###############################################################################

class TodoListView(ListView):
    """Class-based view to show all tasks."""

    model = Todo
    context_object_name = 'todos'
    template_name = 'todos/todo_list_view.html'


###############################################################################
# END
###############################################################################
# Local variables:
# mode: python
# End:
