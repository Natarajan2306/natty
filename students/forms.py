from django.forms import ModelForm
from .models import Database
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class DatabaseForm(ModelForm):
	class Meta:
		model  = Database
		fields = ('companies', 'first_name', 'last_name', 'Title', 'email')

		# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user