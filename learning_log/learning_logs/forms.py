from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        # Overrides Django default form size, widening entry field so user can see
        # their message better
        widgets = {'text': forms.Textarea(attrs = {'cols': 80})}