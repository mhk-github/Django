###############################################################################
# FILE     : update_form.py
# SYNOPSIS : The form for updating a model object.
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

class TodoFormUpdate(forms.ModelForm):
    """A form only used to update an existing task."""

    class Meta:
        model = Todo
        fields = ('task', 'location', 'done')
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


###############################################################################
# END
###############################################################################
# Local variables:
# mode: python
# End:
