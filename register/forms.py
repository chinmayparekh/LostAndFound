from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# from .models import Profile
from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Enter a valid email address.')
    contact = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'contact', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
