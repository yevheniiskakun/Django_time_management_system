from sqlite3 import IntegrityError


from django.db import models


class Shifts(models.Model):
    shift_start_time = models.TimeField()
    shift_end_time = models.TimeField()


    def __str__(self):
        shift_title = str(self.shift_start_time) + "-" + str(self.shift_end_time)
        return shift_title


