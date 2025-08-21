from django.urls import path

from users.views import login, RegisterView, logout

app_name = "users"

urlpatterns = [
    path("login/", login, name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", logout, name="logout")
]
