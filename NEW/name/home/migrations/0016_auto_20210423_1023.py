# Generated by Django 3.1.7 on 2021-04-23 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210423_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu_info',
            name='year',
            field=models.IntegerField(choices=[(2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028)], default=2021, verbose_name='year'),
        ),
        migrations.AlterModelTable(
            name='stu_info',
            table='Stu_infos',
        ),
    ]
