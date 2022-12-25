# Generated by Django 3.2.9 on 2021-11-12 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_user'),
        ('schedules', '0003_remove_schedules_schedule_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee'),
        ),
    ]