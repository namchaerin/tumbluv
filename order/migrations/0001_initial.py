# Generated by Django 3.1.7 on 2021-03-04 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=20)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user')),
            ],
            options={
                'db_table': 'account_numbers',
            },
        ),
        migrations.CreateModel(
            name='CardNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user')),
            ],
            options={
                'db_table': 'card_numbers',
            },
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=40)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user')),
            ],
            options={
                'db_table': 'recipients',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status', models.CharField(max_length=20)),
                ('account_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.accountnumber')),
                ('card_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.cardnumber')),
                ('gift', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.gift')),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.recipient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
