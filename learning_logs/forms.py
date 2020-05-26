from django import forms
from .models import Topic, Entry, UserFile


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
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class DocumentForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ('description', 'document',)
