# Generated by Django 3.2.9 on 2021-11-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0005_alter_shifts_shift_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shifts',
            name='shift_id',
            field=models.IntegerField(),
        ),
    ]
