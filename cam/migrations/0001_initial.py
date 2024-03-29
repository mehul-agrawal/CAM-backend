# Generated by Django 4.0.2 on 2024-03-29 18:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Assignment Name', max_length=256, unique=True)),
                ('performance_date', models.DateField(help_text='Date on which assignment should be performed')),
                ('submission_date', models.DateField(help_text='Date on which assignment should be submitted')),
                ('subject', models.CharField(choices=[('CN', 'Computer Networks'), ('DSA', 'Data Structures and Algorithms')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.IntegerField(help_text='Student roll number')),
                ('spo_marks', models.IntegerField(help_text='SPO Marks', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('rpp_marks', models.IntegerField(help_text='RPP Marks', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('academic_year', models.CharField(choices=[], help_text='Academic Year', max_length=20)),
                ('course', models.CharField(choices=[('CS', 'Computer Science'), ('IT', 'Information Technology')], help_text='course', max_length=20)),
                ('performance_date', models.DateField(help_text='Date on which assignment was performed by student')),
                ('submission_date', models.DateField(help_text='Date on which assignment was submitted by student')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='marks', to='cam.assignment')),
            ],
        ),
    ]
