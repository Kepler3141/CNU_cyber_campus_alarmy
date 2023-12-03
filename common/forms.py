from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    password2 = None
    phone_number = forms.CharField(max_length=15, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("username", "password1", 'phone_number')