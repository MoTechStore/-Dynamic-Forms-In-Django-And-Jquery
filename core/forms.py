from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'id':'emailid'}),
            'course': forms.TextInput(attrs={'class':'form-control', 'id':'courseid'})

        }