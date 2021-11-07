###############################################################################
# FILE     : update_view.py
# SYNOPSIS : The Django 3 class-view to update an existing object is here.
# LICENSE  : MIT
###############################################################################


###############################################################################
# IMPORTS
###############################################################################

from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from todos.forms import TodoFormUpdate
from todos.models import Todo


###############################################################################
# CLASSES
###############################################################################

class TodoUpdateView(UpdateView):
    """Class-based view of a form to update a task."""

    model = Todo
    form_class = TodoFormUpdate
    template_name = 'todos/todo_update_view.html'
    success_url = reverse_lazy('todos:list')


###############################################################################
# END
###############################################################################
# Local variables:
# mode: python
# End:
