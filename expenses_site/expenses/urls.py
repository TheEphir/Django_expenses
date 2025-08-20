from django.urls import path

from expenses.views import ExpensesView, AddExpense

app_name = "expenses"

urlpatterns = [
    path("", ExpensesView.as_view(), name="index"),
    path("add/", AddExpense.as_view(), name="add_expense")
]
