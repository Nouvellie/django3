''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "1.0" 
__created__     =       "12/08/2019 14:16" 
''' 


from .models import Color
from django import forms


import datetime


class ColorForm(forms.ModelForm):


	color_name = forms.CharField(
		required = False,
		label = 'Color name',
		widget=forms.TextInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'COLOR NAME'}
		)
	)

	class Meta:
		model = Color
		fields = (
			'color_name',
		)