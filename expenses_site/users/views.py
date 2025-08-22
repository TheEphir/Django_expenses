from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import UserLoginForm, UserRegistrationForm

# Create your views here.
# class LoginView(TemplateView):
#     template_name = "users/login.html"
#     title = "Expenses - Login"


class UserRegistrationView(SuccessMessageMixin, CreateView):
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    title = "Register - Expense Tracker"
    success_message = "You successfully registered"
    
    def get_success_url(self):
        return reverse_lazy("user:login")
    

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