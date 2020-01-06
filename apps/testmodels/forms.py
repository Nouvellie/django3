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
			attrs = {'class': 'form-control mb-2', 'placeholder': 'NAME',}
		)
	)
	item_image = forms.ImageField(
		required = False,
		label = 'Image',
		widget = forms.ClearableFileInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'IMAGE',}
		)
	)
	item_bool = forms.BooleanField(
		required = False,
		label = 'Bool',
		widget = forms.NullBooleanSelect( # CheckboxInput
			attrs = {'class': 'form-control mb-2',}
		)
	)
	item_date = forms.DateField(
		required = False,
		label = 'Date',
		widget = forms.DateInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'DATE (mm/dd/yyyy)',}
		)
	)
	item_update_date = forms.DateTimeField(
		required = False,
		label = 'Update Date',
		widget = forms.DateInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'UPDATE_DATE (mm/dd/yyyy hh:mm)',}
		)
	)
	item_decimal = forms.DecimalField(
		required = False,
		label = 'Decimal',
		widget = forms.TextInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'DECIMAL',}
		)
	)
	item_email = forms.EmailField(
		required = False,
		label = 'Email',
		widget = forms.EmailInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'EMAIL',}
		)
	)
	item_file = forms.FileField(
		required = False,
		label = 'File',
		widget = forms.ClearableFileInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'FILE',}
		)
	)

	class Meta:
		model = Item
		fields = (
			'item_name',
			'item_image',
			'item_bool',
			'item_date',
			'item_update_date',
			'item_decimal',
			'item_email',
			'item_file',
		)
	
# item_integer
	
# item_slug
	
# item_name
	
# item_url
	
# item_uuid