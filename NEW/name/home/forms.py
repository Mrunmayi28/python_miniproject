from django.core import validators
from django import forms
from django.db.models import fields
from .models import student_add

class student_addform(forms.ModelForm):
    class Meta:
        model = student_add
        fields = ['name' , 'number']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'number' : forms.TextInput(attrs={'class':'form-control'})
        }