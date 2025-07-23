
# Import Django's forms module and User model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Custom user registration form that extends Django's built-in UserCreationForm
# Adds required fields for first name, last name, and email
class CustomUserCreationForm(UserCreationForm):
    # Require first name, last name, email
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    # Meta class to specify the model and fields for the form
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
