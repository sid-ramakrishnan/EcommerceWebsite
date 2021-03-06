import app1

from django import forms
from app1.models import *
from django.core.exceptions import ValidationError
from django.forms.util import ErrorList
from django.http import HttpResponse

class UserForm(forms.Form):
    name    = forms.CharField()
    username = forms.CharField()
    address = forms.CharField()
    email   = forms.EmailField()  
    phone   = forms.IntegerField()
    pwd     = forms.CharField(widget=forms.PasswordInput())

    
    def clean_email(self):
		email=self.cleaned_data['email']
		try:
			Customer.objects.get(email=email)
		except Customer.DoesNotExist:
			return email
		raise forms.ValidationError('An account is already registered under this email.')

    def clean_name(self):
		name=self.cleaned_data['name']
		try:
			Customer.objects.get(name=name)
		except Customer.DoesNotExist:
			return name
		raise forms.ValidationError("A user with that username already exists.")

    def clean_pwd(self):
		pwd=self.cleaned_data['pwd']
		try:
			Customer.objects.get(pwd=pwd)
		except Customer.DoesNotExist:
			return pwd
		raise forms.ValidationError("A user with that password already exists.")	

    def clean_username(self):
                username=self.cleaned_data['username']
		try:
			Customer.objects.get(username=username)
		except Customer.DoesNotExist:
			return username
		raise forms.ValidationError("A user with that username already exists.")


class LoginForm(forms.Form):
	username = forms.CharField()
	pwd = forms.CharField(widget=forms.PasswordInput(),required=False)

	def clean(self):
		username=self.cleaned_data['username']
		pwd = self.cleaned_data['pwd']
		try:
                        Customer.objects.get(username=username,pwd=pwd)
                        return self.cleaned_data
		except Customer.DoesNotExist:
                        self._errors['pwd'] = self.error_class(['Username or password is incorrect.'])



                	
    
