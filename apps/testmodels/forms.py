''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "4.0" 
__created__     =       "12/18/2019 08:50" 
''' 


from .models import Item
from django import forms


class ItemForm(forms.ModelForm):

	item_name = forms.CharField(
		required = False,
		label = 'Name',
		widget = forms.TextInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'NAME'}
		)
	)
	item_image = forms.ImageField(
		required = False,
		label = 'Image',
		widget = forms.ClearableFileInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'NAME'}
		)
	)

	class Meta:
		model = Item
		fields = (
			'',
		)
	
item_bool
	
item_date
	
item_update_date
	
item_decimal
	
item_email
	
item_file
	
item_integer
	
item_slug
	
item_name
	
item_url
	
item_uuid