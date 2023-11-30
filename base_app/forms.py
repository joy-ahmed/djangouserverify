# accounts/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser


# class CustomUserCreationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = CustomUser
#         fields = ['phone_number', 'password', 'email', 'first_name', 'last_name']




class UserLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password']








class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'placeholder':'01000000000', 'class': 'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}))
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'type':'email', 'class': 'form-control'}))
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}))
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = CustomUser
        fields = ('phone_number', 'email', 'first_name', 'last_name', 'profile_picture')


    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')

        # Check if the email is already in use
        if email and CustomUser.objects.filter(email=email).exists():
            self.add_error('email', forms.ValidationError(
                'This email is already in use. Please use a different email.',
                code='duplicate_email',
            ))

        # Check if the phone number is already in use
        if phone_number and CustomUser.objects.filter(phone_number=phone_number).exists():
            self.add_error('phone_number', forms.ValidationError(
                'This phone number is already in use. Please use a different phone number.',
                code='duplicate_phone_number',
            ))

        return cleaned_data
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # Check if the passwords match
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'Passwords do not match. Please enter matching passwords.',
                code='password_mismatch',
            )

        # Check if the password is too short
        if password2 and len(password2) < 8:
            raise forms.ValidationError(
                'Password is too short. Please enter at least 8 characters.',
                code='password_too_short',
            )

        # Check if the password is too common
        common_passwords = ['password', '123456', 'qwerty']  # Add more as needed
        if password2 and password2.lower() in common_passwords:
            raise forms.ValidationError(
                'Password is too common. Please choose a more secure password.',
                code='password_too_common',
            )

        # Check if the password contains at least one digit
        if password2 and not any(char.isdigit() for char in password2):
            raise forms.ValidationError(
                'Password must contain at least one digit.',
                code='password_no_digit',
            )

        # Check if the password contains at least one uppercase letter
        if password2 and not any(char.isupper() for char in password2):
            raise forms.ValidationError(
                'Password must contain at least one uppercase letter.',
                code='password_no_uppercase',
            )

        # Check if the password contains at least one special character
        special_characters = ['!', '@', '#', '$', '%', '^', '&', '*']  # Add more as needed
        if password2 and not any(char in special_characters for char in password2):
            raise forms.ValidationError(
                'Password must contain at least one special character (!, @, #, $, %, ^, &, *).',
                code='password_no_special_character',
            )

        # Add more password checks as needed

        return password2
