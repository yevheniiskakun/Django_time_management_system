# Generated by Django 3.2.9 on 2021-12-27 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_ta_transactions_matches'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TA_transactions',
            new_name='TA_transaction',
        ),
    ]
