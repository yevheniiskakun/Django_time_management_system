#from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # main view
    path('dashboard', views.dashboard, name='dashboard'),
    path('employees', views.employees_view, name='employees'),
    path('schedules', views.schedules_view, name='schedules'),
    path('shifts', views.shifts_view, name='shifts'),
    path('raports/<str:csv_date>', views.raports_view, name='reports'),
    path('raports', views.raports_view, name='reports'),
    path('user_raport/<int:user_pk>', views.user_raport_view, name='user_report'),
    path('logout', views.logout_view, name='logout'),
    path('modify/<int:pk>', views.user_show_all_info, name='user_show_all_info'),
    path('shifts/<int:id>', views.delete_shift, name='delete_shift'),
    path('schedule/<int:id>', views.delete_schedule, name='delete_schedule'),
    path('employee/<int:id>', views.delete_employee, name='delete_employee'),
    path('employee_schedule/<int:pk>', views.employee_schedule, name='employee_schedule'),
]
