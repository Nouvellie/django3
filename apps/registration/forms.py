''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "7.0" 
__created__     =       "01/14/2019 16:21" 
''' 


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormWithEmail(UserCreationForm):

	email = forms.EmailField(
		required = True,
		help_text = "Required, 254 characters maximum and must be valid."
	)

	class Meta:

		model = User
		fields = (
			'username',
			'email',
			'password1',
			'password2',
		)

	def clean_email(self):

		email = self.cleaned_data('email')
		if User.objects.filter(email = email).exists():
			raise forms.ValidationError(
				'The email already exists, please enter a new one.'
			)
		return email