# Generated by Django 3.1.7 on 2021-04-11 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210401_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logged',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]