###############################################################################
# FILE     : delete_view.py
# SYNOPSIS : The Django 3 class-view for deleting existing objects is here.
# LICENSE  : MIT
###############################################################################


###############################################################################
# IMPORTS
###############################################################################

from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from todos.models import Todo


###############################################################################
# CLASSES
###############################################################################

class TodoDeleteView(DeleteView):
    """Class-based view to delete an existing task."""

    model = Todo
    template_name = 'todos/todo_delete_view.html'
    success_url = reverse_lazy('todos:list')


###############################################################################
# END
###############################################################################
# Local variables:
# mode: python
# End:
