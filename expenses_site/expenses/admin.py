from django.contrib import admin

from expenses.models import ExpenseCategory, Expense

# Register your models here.

admin.site.register(ExpenseCategory)

admin.site.register(Expense)