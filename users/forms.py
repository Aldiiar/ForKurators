from django import forms

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(max_length=100, label='name')
    last_name = forms.CharField(max_length=100, label='surname')
    department = forms.CharField(max_length=100, label='department')
    university = forms.CharField(max_length=100, label='university')
    phone_number = forms.CharField(max_length=20, label='phone')
    address = forms.CharField(max_length=200, label='address')
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, label='password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='confirm_password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')

class LoginForm(forms.Form):
    email = forms.CharField(max_length=500)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)