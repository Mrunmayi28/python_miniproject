# Generated by Django 3.1.7 on 2021-05-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20210521_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu_info',
            name='completion_year',
            field=models.IntegerField(default=''),
        ),
    ]
