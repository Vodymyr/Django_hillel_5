from django import forms
from .models import Teacher, Group, Student

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['teacher', 'name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'year']
