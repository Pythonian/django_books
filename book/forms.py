from django import forms

from .models import Request


class RequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your full name'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your email address'})
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter title of the book'})
        self.fields['author'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter name of the author'})

    class Meta:
        model = Request
        fields = ['full_name', 'email', 'title', 'author']
