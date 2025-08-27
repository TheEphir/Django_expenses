from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import TemplateView

from expenses.models import Expense, ExpenseCategory
from expenses.forms import AddExpenseForm, FiltersForm

# Create your views here.
class IndexView(TemplateView):
    template_name = "expenses/index.html"
    title = "Expenses"
    

def user_expenses(request):
    form = FiltersForm()
    expenses = Expense.objects.filter(user=request.user)
   
    # if form.is_valid():
    left_date = request.GET.get("left_date")        
    right_date = request.GET.get("right_date")        
    category = request.GET.get("category")        

    if  left_date:
        expenses = expenses.filter(date__gte=left_date)
    if  right_date:
        expenses = expenses.filter(date__lte=right_date)
    if  category != "All":
        expenses = expenses.filter(category=ExpenseCategory.objects.get(name=category))
        
        
    context = {"expenses": expenses, "form": form}
    return render(request, "expenses/reports.html", context=context)

        
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

