from django import forms
from groups.models import Student

class AddStudentForm(forms.Form):
    photo = forms.ImageField(required=False, label='photo')
    name = forms.CharField(max_length=100, label='name')
    surname = forms.CharField(max_length=100, label='surname')
    phone_number = forms.CharField(max_length=20, label='phone_number')
    date_of_b = forms.DateField(label='date_of_b', widget=forms.DateInput(attrs={'type': 'date'}))


class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['photo', 'name', 'surname', 'phone_number', 'date_of_b']
        widgets = {
            'date_of_b': forms.DateInput(attrs={'type': 'date'}),
        }