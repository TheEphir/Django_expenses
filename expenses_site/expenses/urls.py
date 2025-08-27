from django.urls import path

from expenses.views import user_expenses, add_expense

app_name = "expenses"

urlpatterns = [
    path("", user_expenses, name="index"),
    path("add/", add_expense, name="add_expense")
]
