from pyexpat import model
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
        

class UserRegistrationForm(UserCreationForm):
    class_attr = "w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": class_attr,
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            "class": class_attr,
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": class_attr,
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": class_attr,
        }
    ))
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        return user