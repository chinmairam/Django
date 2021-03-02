from django import forms
from django.forms import ModelForm
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body']
        # exclude = ['timestamp', ]
