from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models
from django import forms
from .models import *
from django import forms
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","first_name","last_name", "email","password1","password2")
        widgets={
        'last_name': forms.TextInput(attrs={'class': 'last_name'}),
        'password':  forms.PasswordInput(attrs={'class': 'password'}),
        
   		 }

class Contact(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
class AddressForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = ('name',
					'email',
					'address', 
					'country',
					'state',
					'zipcode')
        widgets = {
        	'name': forms.TextInput(attrs={'placeholder':'Name'}),
        	'email': forms.TextInput(attrs={'placeholder':'Email'}),
        	'address': forms.TextInput(attrs={'placeholder':'Address'}),
        	'country': forms.TextInput(attrs={'placeholder':'Country'}),
        	'state': forms.TextInput(attrs={'placeholder':'State'}),
        	'zipcode': forms.TextInput(attrs={'placeholder':'ZipCode'}),
        }
    
