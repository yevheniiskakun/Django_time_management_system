# Generated by Django 3.2.9 on 2022-01-02 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0007_auto_20211227_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ta_transaction_processed',
            old_name='matches',
            new_name='late_arrival',
        ),
    ]
