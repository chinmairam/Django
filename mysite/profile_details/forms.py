from django import forms
from .models import User_Profile


class User_Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = '__all__'
