# Generated by Django 5.0.1 on 2024-01-19 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='roll_no',
            new_name='Phone_Number',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='age',
            new_name='Salary',
        ),
    ]
