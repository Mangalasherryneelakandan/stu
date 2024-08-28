from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'middlename', 'lastname', 'course', 'gender', 'phone', 'address', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
