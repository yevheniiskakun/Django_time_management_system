from django import forms


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class TimePickerInput(forms.TimeInput):
    input_type = 'time'


class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'


class ShiftForm(forms.Form):

    shift_start_time = forms.TimeField(widget=TimePickerInput)
    shift_end_time = forms.TimeField(widget=TimePickerInput)