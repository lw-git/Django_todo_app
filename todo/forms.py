from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Add a new task...'}
            )
        }
