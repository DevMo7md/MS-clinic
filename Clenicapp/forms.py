from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'اسم المستخدم'
    }))
    email = forms.EmailField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'البريد الإلكتروني'
    }))
    password1 = forms.CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'كلمة المرور'
    }))
    password2 = forms.CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'تأكيد كلمة المرور'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'اسم المستخدم'
    }))
    password = forms.CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'كلمة المرور'
    }))

