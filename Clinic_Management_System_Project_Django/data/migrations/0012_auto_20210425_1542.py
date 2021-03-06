# Generated by Django 3.1.7 on 2021-04-25 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20210319_1235'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.RemoveField(
            model_name='patientbill',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='patientfeedback',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='prescribed_by',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='prescribed_drug',
        ),
        migrations.DeleteModel(
            name='Drug',
        ),
        migrations.DeleteModel(
            name='PatientBill',
        ),
        migrations.DeleteModel(
            name='PatientFeedback',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
