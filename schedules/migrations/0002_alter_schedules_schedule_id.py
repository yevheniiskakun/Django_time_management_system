# Generated by Django 3.2.9 on 2021-11-10 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='schedule_id',
            field=models.IntegerField(),
        ),
    ]