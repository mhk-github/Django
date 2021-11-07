###############################################################################
# FILE     : create_form.py
# SYNOPSIS : The form for creating a model object.
# LICENSE  : MIT
###############################################################################


###############################################################################
# IMPORTS
###############################################################################

from django import forms
from todos.models import Todo


###############################################################################
# CLASSES
###############################################################################

class TodoFormCreate(forms.ModelForm):
    """A form only used to create a new task."""

    class Meta:
        model = Todo
        fields = ('task', 'location',)
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
        }


###############################################################################
# END
###############################################################################
# Local variables:
# mode: python
# End:
