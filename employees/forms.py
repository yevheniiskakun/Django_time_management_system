from django import forms


class EmployeeForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    employee_pesel = forms.IntegerField()
    employee_join_date = forms.DateField()
    employee_end_date = forms.DateField()
