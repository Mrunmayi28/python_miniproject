# Generated by Django 3.1.7 on 2021-05-13 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20210513_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_add',
            old_name='password',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='student_add',
            name='idNumber',
        ),
    ]
