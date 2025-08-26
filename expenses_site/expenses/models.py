from django.db import models

from users.models import User

# Create your models here.

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Expense(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.01)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.PROTECT)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="expenses", null=True)

    def __str__(self):
        return f"{self.user}: {self.category} - {self.amount}"