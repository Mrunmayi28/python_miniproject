from django.core import validators
from django import forms
from django.db.models import fields
from .models import student_add ,academy

class student_addform(forms.ModelForm):
    class Meta:
        model = student_add
        fields = ['name' , 'number']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'number' : forms.TextInput(attrs={'class':'form-control'})
        }

class student_academy(forms.ModelForm):
    class Meta:
        model = academy 
        fields = ['cgpa','percentage','subject1','subject2','subject3','subject4','subject5','kt']
        widgets = {
            'cgpa' : forms.TextInput(attrs={'class':'form-control'}),
            'percentage' : forms.TextInput(attrs={'class':'form-control'}),
            'subject1' : forms.TextInput(attrs={'class':'form-control'}),
            'subject2' : forms.TextInput(attrs={'class':'form-control'}),
            'subject3' : forms.TextInput(attrs={'class':'form-control'}),
            'subject4' : forms.TextInput(attrs={'class':'form-control'}),
            'subject5' : forms.TextInput(attrs={'class':'form-control'}),
            'kt' : forms.TextInput(attrs={'class':'form-control'})
        }