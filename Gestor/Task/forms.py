from django import forms
from .models import Task, Comment


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add in a new task'}))

    class Meta:
        model = Task
        fields = ('title', 'completed')


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
          'text',
        ]