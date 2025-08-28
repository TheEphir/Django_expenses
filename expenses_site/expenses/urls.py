from django.urls import path

from expenses.views import user_expenses, add_expense, UserExpenses

app_name = "expenses"

urlpatterns = [
    path("", UserExpenses.as_view(), name="index"),
    path("caregory/<str:category>", UserExpenses.as_view(), name="index"),
    path("add/", add_expense, name="add_expense")
]
