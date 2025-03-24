from django import forms

from todo.models import Task
class TasksForm(forms.ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Task
        exclude = ["is_done"]