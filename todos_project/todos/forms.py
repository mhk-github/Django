###############################################################################
# FILE     : forms.py
# SYNOPSIS : All Django forms used are found here.
# LICENSE  : MIT
###############################################################################


###############################################################################
# IMPORTS
###############################################################################

from django import forms
from .models import Todo


###############################################################################
# CLASSES
###############################################################################

class TodoFormCreate(forms.ModelForm):
    """A form only used to create a new task."""

    class Meta:
        model = Todo
        fields = ('task', 'location',)


class TodoFormUpdate(forms.ModelForm):
    """A form only used to update an existing task."""

    class Meta:
        model = Todo
        fields = ('task', 'location', 'done')


###############################################################################
# END
###############################################################################
# Local variables:
# mode: python
# End:
