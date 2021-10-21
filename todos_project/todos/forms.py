from django import forms
from .models import Todo


class TodoFormCreate(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('task', 'location',)

        
class TodoFormUpdate(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('task', 'location', 'done')
