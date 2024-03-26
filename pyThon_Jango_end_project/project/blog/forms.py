from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = {
            'title',
            'content',
            'photo',
            'category',
            'video'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Type Title..."
            }),
            'content': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Type content...'
            }),
            'photo': forms.FileInput(attrs={
                'class': "form-control"
            }),
            'category': forms.Select(attrs={
                'class': "form-control"
            }),
            'video': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Link video'
            })

        }


class loginForm(AuthenticationForm):
    username = forms.CharField(max_length=16, help_text="Maximum 16 words !",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Type Name'
                               }))

    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Type Password'
                               }))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Retry Your Password'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'User Name'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Surname'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2',)
