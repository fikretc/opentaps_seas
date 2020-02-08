# Generated by Django 2.2.9 on 2020-02-06 08:26

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('party', '0001_initial'),
        ('core', '0053_assoc_meter_plan_and_remove_valuation_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.CharField(primary_key=True, max_length=255, verbose_name='Status ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('type', models.CharField(max_length=255, verbose_name='Type')),
                ('description', models.CharField(max_length=255, blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'db_table': 'core_status',
            },
        ),
        migrations.CreateModel(
            name='FinancialTransaction',
            fields=[
                ('financial_transaction_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Financial Transaction ID')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('transaction_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Transaction Date')),
                ('from_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Transaction Billing From Date')),
                ('thru_datetime', models.DateTimeField(null=True, blank=True, verbose_name='Transaction Billing Thru Date')),
                ('transaction_type', models.CharField(max_length=255, verbose_name='Transaction Type')),
                ('source', models.CharField(max_length=255, verbose_name='Source')),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
                ('created_by_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('from_party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='financial_transactions_from', to='party.Party')),
            ],
            options={
                'db_table': 'core_financial_transaction',
            },
        ),
        migrations.CreateModel(
            name='FinancialTransactionHistory',
            fields=[
                ('financial_transaction_history_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Financial Transaction History ID')),
                ('as_of_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='History Date')),
                ('history', models.CharField(blank=True, max_length=255, null=True, verbose_name='History')),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
                ('created_by_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('financial_transaction', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.FinancialTransaction')),
            ],
            options={
                'db_table': 'core_financial_transaction_history',
            },
        ),
        migrations.AddField(
            model_name='financialtransaction',
            name='meter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Meter'),
        ),
        migrations.AddField(
            model_name='financialtransaction',
            name='status',
            field=models.ForeignKey(limit_choices_to={'type': 'transaction'}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.Status'),
        ),
        migrations.AddField(
            model_name='financialtransaction',
            name='to_party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='financial_transactions_to', to='party.Party'),
        ),
        migrations.AddField(
            model_name='financialtransaction',
            name='uom',
            field=models.ForeignKey(limit_choices_to={'type': 'currency'}, on_delete=django.db.models.deletion.DO_NOTHING, verbose_name='Currency', related_name='+', to='core.UnitOfMeasure'),
        ),
    ]
