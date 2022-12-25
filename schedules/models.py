from django.db import models

from employees.models import Employee
from shifts.models import Shifts


class Schedules(models.Model):
    schedule_start_date = models.DateField()
    schedule_end_date = models.DateField()
    shift_id = models.ForeignKey(Shifts, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)


    def __str__(self):
        schedule_title = str(self.schedule_start_date) + " " + str(self.schedule_end_date) + " " + str(self.employee_id)
        return schedule_title


