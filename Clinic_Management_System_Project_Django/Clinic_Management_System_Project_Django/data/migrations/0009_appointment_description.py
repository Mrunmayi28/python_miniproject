# Generated by Django 3.1.7 on 2021-03-17 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_drug_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
