from django import forms
from django.contrib.auth.models import User
from .models import Company, Bus, Location, Route, Ticket, Date, Order


class CreateAccountForm(forms.Form):
    lastname = forms.CharField(initial='Lastname')
    firstname = forms.CharField(initial='Lastname')
    username = forms.CharField(initial='Lastname')
    email = forms.CharField(initial='Lastname')
    password = forms.CharField(initial='Lastname')

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'email', 'password')


class LoginForm(forms.Form):
    username = forms.CharField(initial='Username')
    password = forms.CharField(initial='Password')


class AvailableTicketsForm(forms.Form):
    pass


class PersonalAccountForm(forms.Form):
    pass


class OrderingForm(forms.Form):
    pass





