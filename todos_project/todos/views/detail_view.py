###############################################################################
# FILE     : detail_view.py
# SYNOPSIS : The Django 3 class-view for showing an existing object is here.
# LICENSE  : MIT
###############################################################################


###############################################################################
# IMPORTS
###############################################################################

from django.views.generic.detail import DetailView

from todos.models import Todo


###############################################################################
# CLASSES
###############################################################################

class TodoDetailView(DetailView):
    """Class-based view to show a single task."""

    model = Todo
    context_object_name = 'todo'
    template_name = 'todos/todo_detail_view.html'


###############################################################################
# END
###############################################################################
# Local variables:
# mode: python
# End:
