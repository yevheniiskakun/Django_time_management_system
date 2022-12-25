from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_PESEL = models.IntegerField()
    employment_join_date = models.DateField()
    employment_end_date = models.DateField()

    def __str__(self):
        schedule_title = str(self.user.first_name) + " " + str(self.user.last_name)
        return schedule_title
