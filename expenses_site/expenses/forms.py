from django import forms
from expenses.models import Expense

CHOISES = [
    ("Food","Food"),
    ("Transport","Transport"),
    ("Entertainment","Entertainment"),
    ("Bills","Bills"),
    ("Other","Other"),
]

FILTERS = [
    ("All","All Categories"),
    ("Food","Food"),
    ("Transport","Transport"),
    ("Entertainment","Entertainment"),
    ("Bills","Bills"),
    ("Other","Other"),
]

class AddExpenseForm(forms.Form):
    amount = forms.DecimalField( 
        min_value=0.01, 
        widget=forms.NumberInput(attrs={"class":"w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600", "step":"0.01"}),
        required=True,
        )
    category = forms.CharField(
        widget=forms.Select(attrs={"class":"w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"}, choices=CHOISES),
        required=True
        )
    date = forms.DateField(
        widget=forms.DateInput(attrs={"type":"date","class":"w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"}),
        required=True
        )
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class":"w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"}),
        required=False
        )
    
    class Meta:
        model = Expense
        fields = ["amount", "category", "date", "description"]
        

class FiltersForm(forms.Form):
    left_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type":"date", "class":"w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"})
    )
    right_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type":"date", "class":"w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"})
    )
    category = forms.CharField(
        required=False,
        widget=forms.Select(attrs={"class":"w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"}, choices=FILTERS),
    )
    
    class Meta:
        # model = Expense
        fields = ["left_date", "right_date", "category"]