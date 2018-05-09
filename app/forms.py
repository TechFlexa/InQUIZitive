from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm 


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=User
		fields=('first_name','email','username','password','confirm_password')