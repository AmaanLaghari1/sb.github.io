from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
# from .models import UserInfo

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': 'true', 'id': 'floatingInput'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'required': 'true', 'id': 'floatingInput'}), label='Confirm Password')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'floatingInput', 'required': 'true'}), 'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'id': 'floatingInput', 'required': 'true'}), 'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'id': 'floatingInput', 'required': 'true'}), 'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'floatingInput', 'required': 'true', 'name': 'email'})}

class LogInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'floatingInput'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': 'true', 'id': 'floatingInput'}))
