# Generated by Django 5.0.6 on 2024-06-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_rename_time_stamp_transaction_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_bankrupt',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Deposit'), (2, 'Withdrawal'), (3, 'Loan'), (4, 'Loan Paid'), (5, 'Transfer Balance')], null=True),
        ),
    ]
