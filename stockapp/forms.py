from django import forms
from django.contrib.auth.forms import UserCreationForm

from stockapp.models import Login, Customer, Stock


class Loginform(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ('user',)


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'

