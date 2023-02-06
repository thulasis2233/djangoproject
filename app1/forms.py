from django import forms
from . models import submit,Images

class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=submit
        fields=('Email','Password')
class SignupForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=submit
        fields='__all__'
    
class UpdateForm(forms.ModelForm):
    class Meta():
        model=submit
        fields=('Name','Age','Place','Email')
    
class ImageForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Images
        fields='__all__'