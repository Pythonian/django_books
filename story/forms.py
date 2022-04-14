from django import forms

from .models import Story, Chapter


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['poster', 'title', 'category', 'description']


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'body']


class StoryDeleteForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = []
