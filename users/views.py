import os

from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from employees.models import Employee
from praca.settings import BASE_DIR
from schedules.models import Schedules
from shifts.models import Shifts
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from shifts.forms import ShiftForm
from shifts.models import Shifts
from django.contrib.auth.decorators import login_required

from schedules.forms import ScheduleForm
from schedules.models import Schedules

from employees.forms import EmployeeForm
from employees.models import Employee

from django.db.models import Count

import csv
from datetime import datetime, date, timedelta
from transaction.models import TA_transaction, TA_transaction_processed, Statistics
import time



import random
import string

import pandas as pd

user_password_length = 8


@login_required
def dashboard(request):
    employees = Employee.objects.all()[:5]
    schedules = Schedules.objects.all()
    shifts = Shifts.objects.all()
    amount_of_proccessed_transactions = Statistics.objects.get(pk=1).amount_of_proccessed_transactions
    context = {"employees": employees, "schedules": schedules, "shifts": shifts,
               'transactions': amount_of_proccessed_transactions}
    return render(request, "users/dashboard.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")

@login_required
def user_show_all_info(request, pk):


    employee = Employee.objects.get(pk=pk)
    user = User.objects.get(employee=employee)

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        employee_pesel = request.POST['employee_pesel']
        employment_join_date = request.POST['employee_join_date']
        employment_end_date = request.POST['employee_end_date']
        employee.employee_PESEL = employee_pesel
        employee.employment_join_date = employment_join_date
        employee.employment_end_date = employment_end_date
        employee.save()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        return redirect('/users/modify/' + str(pk))
    else:
        pass

    context = {"employee": employee, "user": user}
    return render(request, "users/user_modify.html", context)

@login_required
def employees_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        employee_form = EmployeeForm(request.POST)
        # check whether it's valid:
        if employee_form.is_valid():
            first_name = employee_form.cleaned_data['first_name']
            last_name = employee_form.cleaned_data['last_name']
            email = employee_form.cleaned_data['email']
            employee_pesel = employee_form.cleaned_data['employee_pesel']
            employment_join_date = employee_form.cleaned_data['employee_join_date']
            employment_end_date = employee_form.cleaned_data['employee_end_date']
            username = email
            password_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            temp = random.sample(password_set, user_password_length)
            user_password = "".join(temp)
            new_user = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email,
                                                  username=username, password=user_password)
            new_employee = Employee.objects.get_or_create(user=new_user[0], employee_PESEL=employee_pesel,
                                                          employment_join_date=employment_join_date,
                                                          employment_end_date=employment_end_date)
            return redirect('/users/employees')

        # if a GET (or any other method) we'll create a blank form
    else:
        employee_form = EmployeeForm()

    employees = Employee.objects.all()
    context = {"employees": employees, "employee_form": employee_form}
    return render(request, "users/employees.html", context)


@login_required
def employee_schedule(request, pk):

    shift = Shifts.objects.filter(pk=pk).first()
    schedule_list = Schedules.objects.filter(shift_id=pk)
    context = {"schedule_list": schedule_list, "shift": shift}
    return render(request, "users/employees_schedule.html", context)


@login_required
def schedules_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        scheduleform = ScheduleForm(request.POST)
        # check whether it's valid:
        if scheduleform.is_valid():
            schedule_start_date = scheduleform.cleaned_data['schedule_start_date']
            schedule_end_date = scheduleform.cleaned_data['schedule_end_date']
            shift = scheduleform.cleaned_data['shift']
            employee = scheduleform.cleaned_data['employee']
            Schedules.objects.get_or_create(schedule_start_date=schedule_start_date,
                                            schedule_end_date=schedule_end_date, shift_id=shift, employee_id=employee)
            return redirect('/users/schedules')

        # if a GET (or any other method) we'll create a blank form
    else:
        scheduleform = ScheduleForm()

    schedules = Schedules.objects.all()

    context = {"schedules": schedules, "scheduleform": scheduleform}
    return render(request, "users/schedules.html", context)


@login_required
def shifts_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        shiftform = ShiftForm(request.POST)
        # check whether it's valid:
        if shiftform.is_valid():
            shift_start_time = shiftform.cleaned_data['shift_start_time']
            shift_end_time = shiftform.cleaned_data['shift_end_time']
            Shifts.objects.get_or_create(shift_start_time=shift_start_time, shift_end_time=shift_end_time)
            return redirect('/users/shifts')

        # if a GET (or any other method) we'll create a blank form
    else:
        shiftform = ShiftForm()

    shifts = Shifts.objects.all()
    context = {"shifts": shifts, "shiftform": shiftform}
    return render(request, "users/shifts.html", context)


def delete_shift(request, id):
    Shifts.objects.filter(id=id).delete()
    return redirect('/users/shifts')


def delete_schedule(request, id):
    Schedules.objects.filter(id=id).delete()
    return redirect('/users/schedules')


def delete_employee(request, id):
    Employee.objects.filter(id=id).delete()
    return redirect('/users/employees')


@login_required
def raports_view(request, csv_date=''):
    today_csv_raport_path = "transaction_csv/" + str(datetime.today().strftime('%Y-%m-%d')) + ".csv"

    try:
        with open(today_csv_raport_path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in csv_reader:
                readed_row = ', '.join(row)
                readed_list = readed_row.split(",")
                transaction = TA_transaction.objects.get_or_create(employee_id=readed_list[0],
                                                                   time_in=str(readed_list[1]),
                                                                   time_out=str(readed_list[2]))
                # TA_transaction.objects.all().delete()
                try:
                    employee = Employee.objects.get(employee_PESEL=readed_list[0])
                    schedules = Schedules.objects.filter(employee_id=employee)
                except:
                    schedules = {}
                # print(schedule)
                # print(schedule.schedule_start_date)
                # print(schedule.schedule_end_date)
                # print(datetime.strptime(datetime.today().strftime('%Y-%m-%d'), '%Y-%m-%d').date())
                for schedule in schedules:
                    if schedule.schedule_end_date >= datetime.strptime(datetime.today().strftime('%Y-%m-%d'),
                                                                       '%Y-%m-%d').date():
                        # print(schedule)
                        if schedule.schedule_end_date >= datetime.strptime(datetime.today().strftime('%Y-%m-%d'),
                                                                           '%Y-%m-%d').date() >= schedule.schedule_start_date:
                            shift = str(schedule.shift_id)
                            shift_list = shift.split("-")
                            # print(readed_list)
                            # print(shift_list)
                            shift_start_work_time = datetime.strptime(str(shift_list[0]), '%H:%M:%S').time()
                            shift_end_work_time = datetime.strptime(str(shift_list[1]), '%H:%M:%S').time()
                            actual_start_work_time = datetime.strptime(str(readed_list[1]), '%H:%M:%S').time()
                            actual_end_work_time = datetime.strptime(str(readed_list[2]), '%H:%M:%S').time()
                            now = datetime.now()
                            db_gap = Statistics.objects.get(pk=1).late_gap
                            gap = timedelta(minutes=int(db_gap))
                            start_work_delta = datetime.combine(date.today(),
                                                                actual_start_work_time) - datetime.combine(
                                date.today(), shift_start_work_time)
                            end_work_delta = datetime.combine(date.today(), shift_end_work_time) - datetime.combine(
                                date.today(),
                                actual_end_work_time)
                            # print("start_work_delta: ", start_work_delta)
                            # print("end_work_delta: ", end_work_delta)
                            late_arrival = False
                            late_leaving = False
                            final_in_time = ''
                            final_out_time = ''
                            # print("actual_start_work_time: ", actual_start_work_time)
                            # print("actual_end_work_time: ", actual_end_work_time)
                            # print("shift_start_work_time: ", shift_start_work_time)
                            # print("shift_end_work_time: ", shift_end_work_time)
                            # print("start_work_delta: ", start_work_delta)
                            if start_work_delta <= gap:
                                # print("start_work_time: ", shift_start_work_time)
                                final_in_time = shift_start_work_time
                            elif start_work_delta > gap:
                                # print("actual_start_work_time: ", actual_start_work_time)
                                late_arrival = True
                                final_in_time = actual_start_work_time

                            if end_work_delta <= gap:
                                # print("end_work_time: ", shift_end_work_time)
                                final_out_time = shift_end_work_time
                            elif end_work_delta > gap:
                                # print("actual_end_work_time: ", actual_end_work_time)
                                late_leaving = True
                                final_out_time = actual_end_work_time
                            # print("final_in_time: ", final_in_time)
                            # print("final_out_time: ", final_out_time)
                            working_time = datetime.combine(date.today(), final_out_time) - datetime.combine(
                                date.today(), final_in_time)
                            try:
                                working_time = datetime.strptime(str(working_time), '%H:%M:%S').time()
                            except ValueError:
                                working_time = str(working_time).replace("-1 day, ", "")
                            # print("working_time: ", working_time)
                            # print("late_arrival: ", late_arrival)
                            # print("late_leaving: ", late_leaving)
                            processed_transaction = TA_transaction_processed.objects.create(
                                employee_id=employee.employee_PESEL,
                                time_in=final_in_time,
                                time_out=final_out_time,
                                working_time=str(working_time),
                                late_arrival=late_arrival,
                                late_leaving=late_leaving)
                            statistics_TA = Statistics.objects.get(pk=1)
                            statistics_TA.amount_of_proccessed_transactions = int(
                                statistics_TA.amount_of_proccessed_transactions) + 1
                            statistics_TA.save()

                else:
                    pass

    except FileNotFoundError:
        print("Can not find today csv")

    # Deleting the csv file

    if (os.path.exists(today_csv_raport_path) and os.path.isfile(today_csv_raport_path)):
        os.remove(today_csv_raport_path)
        print("Today csv file was deleted")
    else:
        print("Can not delete today csv because it is not found")

    if csv_date == "0":
        processed_transactions = TA_transaction_processed.objects.all().order_by('transaction_date')
    elif csv_date == "1":
        processed_transactions = TA_transaction_processed.objects.all().order_by('-transaction_date')
    elif csv_date == "2":
        processed_transactions = TA_transaction_processed.objects.all()[:7]
    elif len(csv_date) >= 2:
        processed_transactions = TA_transaction_processed.objects.filter(transaction_date=csv_date)
    else:
        processed_transactions = TA_transaction_processed.objects.all()

    if request.method == 'POST':
        date_from = request.POST['date_from']
        date_to = request.POST['date_to']
        convert_to_excel = request.POST.get('convert_to_excel', 'off')
        # print(convert_to_excel)
        # print(date_from, date_to)
        transaction_excel = []
        if date_from != "" and date_to != "":
            processed_transactions = TA_transaction_processed.objects.filter(
                transaction_date__range=[date_from, date_to])
            for transaction in processed_transactions:
                # print(transaction.employee_id)
                employee = Employee.objects.get(employee_PESEL=int(transaction.employee_id))
                user = User.objects.get(email=employee.user)
                user_info = user.first_name + " " + user.last_name
                excel_dict = {'employee_id': transaction.employee_id, 'employee_info': user_info,
                              'time_in': transaction.time_in.strftime("%H:%M:%S"),
                              'time_out': transaction.time_out.strftime("%H:%M:%S"),
                              'working_time': transaction.working_time.strftime("%H:%M:%S"),
                              'transaction_date': transaction.transaction_date.strftime('%Y-%m-%d')}
                transaction_excel.append(excel_dict)

                # print(excel_dict)
                if convert_to_excel == "on":
                    df = pd.DataFrame.from_dict(transaction_excel)
                    # print(df)
                    excel_name = str(date_from) + " " + str(date_to) + " " + str(
                        datetime.today().strftime('%Y-%m-%d')) + ".xlsx"
                    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", excel_name)
                    df.to_excel(excel_name)
                    df.to_excel(desktop_path)


    transactions_dates = TA_transaction_processed.objects.all().values('transaction_date').distinct()



    context = {"processed_transactions": processed_transactions, 'transactions_dates': transactions_dates}
    return render(request, "users/raports.html", context)


@login_required
def user_raport_view(request, user_pk):

    try:
        employee = Employee.objects.get(employee_PESEL=user_pk)
        transactions = TA_transaction_processed.objects.filter(employee_id=user_pk)

        if request.method == 'POST':
            date_from = request.POST['date_from']
            date_to = request.POST['date_to']
            # print(date_from, date_to)
            if date_from != "" and date_to != "":
                transactions = TA_transaction_processed.objects.filter(transaction_date__range=[date_from, date_to])

    except:
        employee = 1
        transactions = 1

    context = {'transactions': transactions, 'employee': employee}
    return render(request, "users/user_raport.html", context)
