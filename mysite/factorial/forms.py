from django import forms
from django.forms import ModelForm
from .models import FactorialPost


class FactorialForm(forms.ModelForm):
    class Meta:
        model = FactorialPost
        fields = ['num', 'res']
