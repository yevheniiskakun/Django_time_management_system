# Generated by Django 3.2.9 on 2021-12-27 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_alter_ta_transactions_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ta_transactions',
            name='matches',
            field=models.BooleanField(default=False),
        ),
    ]
