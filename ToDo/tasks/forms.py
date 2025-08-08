from .models import Task, Comment
from django import forms


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
          'caption'
        ]


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
          'text',
        ]