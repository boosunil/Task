from django import forms
from django.forms import ModelForm
from newapp.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
