# Generated by Django 3.2.9 on 2021-12-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_remove_ta_transaction_matches'),
    ]

    operations = [
        migrations.CreateModel(
            name='TA_transaction_processed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
                ('matches', models.BooleanField(default=False)),
                ('transaction_id', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='ta_transaction',
            name='time_in',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='ta_transaction',
            name='time_out',
            field=models.TimeField(),
        ),
    ]
