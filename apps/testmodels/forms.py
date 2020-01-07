''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "4.0" 
__created__     =       "12/18/2019 08:50" 
''' 


from .choice import choices_random
from .models import Item
from django import forms


class ItemForm(forms.ModelForm):

	item_name = forms.CharField(
		required = False,
		label = 'Name',
		widget = forms.TextInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'NAME',}
		),
	)
	item_image = forms.ImageField(
		required = False,
		label = 'Image',
		widget = forms.ClearableFileInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'IMAGE',}
		),
	)
	item_bool = forms.BooleanField(
		required = False,
		label = 'Bool',
		widget = forms.NullBooleanSelect( # CheckboxInput
			attrs = {'class': 'form-control mb-2',}
		),
	)
	item_date = forms.DateField(
		required = False,
		label = 'Date',
		widget = forms.DateInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'DATE (mm/dd/yyyy)',}
		),
	)
	item_update_date = forms.DateTimeField(
		required = False,
		label = 'Update Date',
		widget = forms.DateInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'UPDATE_DATE (mm/dd/yyyy hh:mm)',}
		),
	)
	item_decimal = forms.DecimalField(
		required = False,
		label = 'Decimal',
		widget = forms.TextInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'DECIMAL',}
		),
	)
	item_email = forms.EmailField(
		required = False,
		label = 'Email',
		widget = forms.EmailInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'EMAIL',}
		),
	)
	item_file = forms.FileField(
		required = False,
		label = 'File',
		widget = forms.ClearableFileInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'FILE',}
		),
	)
	item_integer = forms.IntegerField(
		required = False,
		label = 'Integer',
		widget = forms.TextInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'INTEGER',}
		),
	)
	item_slug = forms.SlugField(
		required = False,
		label = 'Slug',
		widget = forms.TextInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'SLUG',}
		),	
	)
	item_url = forms.URLField(
		required = False,
		label = 'URL',
		widget = forms.URLInput(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'URL',}
		),
	)
	# item_uuid = forms.UUIDField(
	# 	required = False,
	# 	label = 'UUID',
	# 	widget = forms.TextInput(
	# 		attrs = {'class': 'form-control mb-2', 'placeholder': 'UUID',}
	# 	)	
	# ),
	item_text = forms.CharField(
		required = False,
		label = 'Text',
		widget = forms.Textarea(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'TEXT',}
		),
	)
	item_choices = forms.ChoiceField(
		required = False,
		label = 'Choices',
		widget = forms.Select(
			attrs = {'class': 'form-control mb-2', 'placeholder': 'CHOICES',}
		),
		choices = choices_random,
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
			'item_integer',
			'item_slug',
			'item_url',
			# 'item_uuid',
			'item_text',
			'item_choices',
		)

# UUID is create by default. If you want to create it manually, mute the default in models and demote uuid in forms.