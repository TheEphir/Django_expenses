from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse

from users.forms import UserLoginForm

# Create your views here.
# class LoginView(TemplateView):
#     template_name = "users/login.html"
#     title = "Expenses - Login"


class RegisterView(TemplateView):
    template_name = "users/register.html"
    title = "Register - Expense Tracker"
    

def login (request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            
            print(request.POST)
            
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("index"))
    else:
        form = UserLoginForm()
    
    context = {"form":form}
    return render(request, "users/login.html", context=context)

        


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))