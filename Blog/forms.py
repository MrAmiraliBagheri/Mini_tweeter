from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Tweet
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
