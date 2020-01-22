''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "7.0" 
__created__     =       "01/14/2019 16:21" 
''' 


from .forms import UserCreationFormWithEmail
from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):

	form_class = UserCreationFormWithEmail
	template_name = 'registration/registration_form.html'

	def get_form(self, form_class = None):

		form = super(SignUpView, self).get_form()

		form.fields['username'].widget = forms.TextInput(
			attrs = {
				'placeholder': 'username',
			},
		)
		form.fields['email'].widget = forms.EmailInput(
			attrs = {
				'placeholder': 'email',
			},
		)
		form.fields['password1'].widget = forms.PasswordInput(
			attrs = {
				'placeholder': 'password',
			},
		)
		form.fields['password2'].widget = forms.PasswordInput(
			attrs = {
				'placeholder': 'repeat password',
			},
		)
		return form

	def get_success_url(self):
		return reverse_lazy('login') + '?register'