from django import forms
from shifts.models import Shifts
from employees.models import Employee


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class TimePickerInput(forms.TimeInput):
    input_type = 'time'


class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'


class ScheduleForm(forms.Form):
    schedule_start_date = forms.DateField(widget=DatePickerInput)
    schedule_end_date = forms.DateField(widget=DatePickerInput)
    shift = forms.ModelChoiceField(queryset=Shifts.objects.all(), empty_label=None)
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label=None)