# Generated by Django 3.2.16 on 2022-12-27 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_student_first_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Database',
        ),
    ]
