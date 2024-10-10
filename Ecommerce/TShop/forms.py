from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    telephone = forms.CharField(max_length=12, help_text='Required. Enter your telephone number.')

    class Meta:
        model = User
        fields = ('username', 'email', 'telephone', 'password1', 'password2')
