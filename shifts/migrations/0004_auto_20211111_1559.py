# Generated by Django 3.2.9 on 2021-11-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0003_auto_20211111_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shifts',
            name='shift_end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='shifts',
            name='shift_start_time',
            field=models.TimeField(),
        ),
    ]
