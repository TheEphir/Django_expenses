from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from expenses.models import Expense, ExpenseCategory
from expenses.forms import AddExpenseForm, FiltersForm

# Create your views here.
class IndexView(TemplateView):
    template_name = "expenses/index.html"
    title = "Expenses"
    
# for now it's don't work
class UserExpenses(ListView):
    model = Expense
    template_name = "expenses/reports.html"
    
    def get_queryset(self):
        queryset = super(UserExpenses, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        left_date = self.request.GET.get("left_date")
        right_date = self.request.GET.get("right_date")        
        category = self.request.GET.get("category")        
        
        if  left_date:
            queryset = queryset.filter(date__gte=left_date)
        if  right_date:
            queryset = queryset.filter(date__lte=right_date)
        if  category:
            queryset = queryset.filter(category=ExpenseCategory.objects.get(name=category))
        print(category)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(UserExpenses, self).get_context_data(**kwargs)
        expenses = Expense.objects.filter(user=self.request.user)
    
        total_amount = 0
        for item in expenses:
            total_amount += item.amount
        
                
        context["total_amount"] = total_amount
        context["expenses"] = expenses
        context["form"] = FiltersForm()

        return context
        


def user_expenses(request):
    form = FiltersForm()
    expenses = Expense.objects.filter(user=request.user)
   
    left_date = request.GET.get("left_date")        
    right_date = request.GET.get("right_date")        
    category = request.GET.get("category")        

    if  left_date:
        expenses = expenses.filter(date__gte=left_date)
    if  right_date:
        expenses = expenses.filter(date__lte=right_date)
    if  category:
        expenses = expenses.filter(category=ExpenseCategory.objects.get(name=category))
        
    total_amount = 0
    
    for item in expenses:
        total_amount += item.amount
    
    context = {"expenses": expenses, "form": form, "total_amount": total_amount}
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

