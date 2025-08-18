from django.db import models

# Create your models here.

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Expense(models.Model):
    ammont = models.DecimalField(decimal_places=2)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.PROTECT)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)