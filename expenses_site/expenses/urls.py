from django.urls import path

from expenses.views import ExpensesView, add_expense

app_name = "expenses"

urlpatterns = [
    path("", ExpensesView.as_view(), name="index"),
    path("add/", add_expense, name="add_expense")
]
