import datetime

from django.db import models

import random

from employees.models import Employee


class TA_transaction(models.Model):
    employee_id = models.IntegerField()
    time_in = models.TimeField()
    time_out = models.TimeField()
    transaction_id = models.IntegerField()

    def __str__(self):
        return str(self.transaction_id)

    def save(self, *args, **kwargs):
        random_key = random.randint(1000, 9999)
        self.transaction_id = int(str(self.employee_id) + str(random_key))
        super(TA_transaction, self).save(*args, **kwargs)


class TA_transaction_processed(models.Model):
    employee_id = models.IntegerField()
    time_in = models.TimeField()
    time_out = models.TimeField()
    working_time = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.time(0, 00))
    transaction_date = models.DateField(auto_now=True)
    late_arrival = models.BooleanField(default=False)
    late_leaving = models.BooleanField(default=False)
    transaction_id = models.IntegerField()

    def __str__(self):
        return str(self.transaction_id)

    def save(self, *args, **kwargs):
        random_key = random.randint(1000, 9999)
        self.transaction_id = int(str(self.employee_id) + str(random_key))
        super(TA_transaction_processed, self).save(*args, **kwargs)


class Statistics(models.Model):
    amount_of_proccessed_transactions = models.IntegerField()
    late_gap = models.IntegerField(default=15, blank=False)

    def __str__(self):
        return str(self.id)