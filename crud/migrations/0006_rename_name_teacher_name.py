# Generated by Django 5.0.1 on 2024-01-20 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_rename_roll_no_teacher_phone_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='name',
            new_name='Name',
        ),
    ]
