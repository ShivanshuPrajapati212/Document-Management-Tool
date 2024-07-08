# forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'file']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full bg-gray-100 px-4 py-2 rounded-lg focus:outline-none',
                'placeholder': 'Title',
            }),
            'file': forms.FileInput(attrs={
                'class': 'w-full bg-gray-100 px-4 py-2 rounded-lg focus:outline-none',
            }),
        }
