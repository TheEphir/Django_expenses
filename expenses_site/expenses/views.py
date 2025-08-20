from django.shortcuts import render
from django.views.generic.base import TemplateView

from expenses.models import Expense

# Create your views here.
class IndexView(TemplateView):
    template_name = "expenses/index.html"
    title = "Expenses"
    

class ExpensesView(TemplateView):
    model = Expense
    template_name = "expenses/reports.html"
    title = "Expenses Report"


class AddExpense(TemplateView):
    model = Expense
    template_name = "expenses/add_expense.html"