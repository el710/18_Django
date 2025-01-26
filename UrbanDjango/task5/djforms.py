
from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(label="Введите логин: ", required=True, max_length="100")
    userpass = forms.CharField(label="Введите пароль: ", required=True, min_length="8", widget=forms.PasswordInput)
    userrepass = forms.CharField(label="Повторите пароль: ", required=True, min_length="8", widget=forms.PasswordInput)
    userage = forms.DecimalField(label="Введите свой возраст: ", max_value=100)
    