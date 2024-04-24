from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=5)
    password1 = forms.CharField(widget=forms.PasswordInput(), min_length=3)
    password2 = forms.CharField(widget=forms.PasswordInput(), min_length=3)