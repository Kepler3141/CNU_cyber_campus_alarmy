from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser

class UserForm(UserCreationForm):
    # email = forms.EmailField(label="이메일")
    phone_number = forms.CharField(max_length=15, required=False, help_text='Optional.')
    password2 = None

    class Meta:
        model = User
        fields = ("username", "password1", "phone_number")