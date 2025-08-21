from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600",
            "placeholder":"Enter your login"
            }
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class":"w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600",
            "placeholder":"Enter your password"
            }
        ))
    
    class Meta:
        model = User
        fields = ["username", "password"]