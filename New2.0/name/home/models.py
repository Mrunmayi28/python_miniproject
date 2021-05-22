from django.db import models
import datetime

# Create your models here.

class certi(models.Model):
    internship = models.FileField()
    course = models.FileField()
    
class formed(models.Model):
    Name = models.CharField(max_length=30)
    Contact=models.CharField(max_length=40)
    email=models.EmailField()
    class Meta:
        db_table = "Formeds"

class academy(models.Model):
    cgpa = models.FloatField(max_length=70)
    percentage = models.FloatField(max_length=70)
    subject1 = models.FloatField(max_length=70)
    subject2 = models.FloatField(max_length=70)
    subject3 = models.FloatField(max_length=70)
    subject4 = models.FloatField(max_length=70)
    subject5 = models.FloatField(max_length=70)
    kt       = models.FloatField(max_length=70)

class stu_info(models.Model):
    idNumber = models.IntegerField()
    roll = models.IntegerField()
    department = models.CharField(max_length=10)
    student_name = models.CharField(max_length=10)
    father_name = models.CharField(max_length=10)
    mother_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    photo = models.FileField(null = True)
    sign = models.FileField(null = True)
    dob = models.DateField()
    student_email = models.EmailField()
    phone = models.IntegerField()
    completion_year = [(r,r) for r in range(2021, datetime.date.today().year+8)]
    year = models.IntegerField(('year'), choices=completion_year, default=datetime.datetime.now().year)
    address = models.CharField(max_length=20)
    country = models.CharField(max_length=10)
    state = models.CharField(max_length=15)
    district = models.CharField(max_length=10)
    email_mother = models.EmailField()
    email_father = models.EmailField()
    number_father = models.IntegerField()
    number_mother = models.IntegerField()
    designation_mother = models.CharField(max_length=20)
    designation_father = models.CharField(max_length=20)
    class Meta:
        db_table = "Stu_infos"

class student_add(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=70)