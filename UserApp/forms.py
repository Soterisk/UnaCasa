from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):

    tel_num = forms.CharField(max_length=20, required=False, help_text='Optional.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'tel_num')
