# Generated by Django 3.2.9 on 2021-11-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0004_auto_20211111_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shifts',
            name='shift_id',
            field=models.IntegerField(default=1),
        ),
    ]
