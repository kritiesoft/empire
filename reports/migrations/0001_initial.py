# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.PositiveIntegerField()),
                ('updated_date', models.DateTimeField()),
                ('updated_by', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'ebc_categories',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.PositiveIntegerField()),
                ('updated_date', models.DateTimeField()),
                ('updated_by', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'ebc_department',
            },
        ),
        migrations.CreateModel(
            name='EmployeeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.PositiveIntegerField()),
                ('updated_date', models.DateTimeField()),
                ('updated_by', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'ebc_employee_status',
            },
        ),
        migrations.CreateModel(
            name='EmployeeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_type', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.PositiveIntegerField()),
                ('updated_date', models.DateTimeField()),
                ('updated_by', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'ebc_employee_table',
            },
        ),
        migrations.CreateModel(
            name='InquiryActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.PositiveIntegerField()),
                ('updated_date', models.DateTimeField()),
                ('updated_by', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'ebc_inquiry_activity',
            },
        ),
        migrations.CreateModel(
            name='InquirySources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sources', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.PositiveIntegerField()),
                ('updated_date', models.DateTimeField()),
                ('updated_by', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'ebc_inquiry_services',
            },
        ),
        migrations.CreateModel(
            name='InquiryStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.PositiveIntegerField()),
                ('updated_date', models.DateTimeField()),
                ('updated_by', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'ebc_inquiry_status',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('create_by', models.PositiveIntegerField()),
                ('updated_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'ebc_location',
            },
        ),
        migrations.CreateModel(
            name='NotificationReadLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'ebc_notification_read_log',
            },
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=200, null=True)),
                ('imagePath', models.URLField(max_length=500, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.PositiveIntegerField()),
                ('updated_date', models.DateTimeField()),
                ('updated_by', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'ebc_notifications',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200, null=True)),
                ('response_time', models.PositiveIntegerField()),
                ('threshold_time', models.PositiveIntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.PositiveIntegerField()),
                ('updated_date', models.DateTimeField()),
                ('updated_by', models.PositiveIntegerField()),
                ('category', models.ManyToManyField(to='reports.Categories')),
            ],
            options={
                'db_table': 'ebc_services',
            },
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.PositiveIntegerField()),
                ('updated_date', models.DateTimeField()),
                ('updated_by', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'ebc_task_status',
            },
        ),
        migrations.AddField(
            model_name='notificationreadlog',
            name='notification',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reports.Notifications'),
        ),
    ]