# accounts/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'password', 'email', 'first_name', 'last_name']




class UserLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
