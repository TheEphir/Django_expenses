from django.urls import path

from users.views import login, UserRegistrationView, logout

app_name = "users"

urlpatterns = [
    path("login/", login, name="login"),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("logout/", logout, name="logout")
]
