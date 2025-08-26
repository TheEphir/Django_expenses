from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import TemplateView

from expenses.models import Expense, ExpenseCategory
from expenses.forms import AddExpenseForm

# Create your views here.
class IndexView(TemplateView):
    template_name = "expenses/index.html"
    title = "Expenses"
    

class ExpensesView(TemplateView):
    model = Expense
    template_name = "expenses/reports.html"
    title = "Expenses Report"


def add_expense(request):
    if request.method == "POST":
        pass
        form = AddExpenseForm(data=request.POST)
        if form.is_valid():
            amount = float(request.POST["amount"])
            category = ExpenseCategory.objects.get(name=request.POST["category"])
            date = request.POST["date"]
            description = request.POST["description"]
            user = request.user
            Expense.objects.create(amount=amount, category=category, date = date, description=description, user=user)
            return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else:
        form = AddExpenseForm()
        
    context = {"form":form}
    return render(request, "expenses/add_expense.html", context=context)

