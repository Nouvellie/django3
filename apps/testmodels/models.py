''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "4.0" 
__created__     =       "12/18/2019 08:50" 
''' 


from django.core.validators import (
	MinValueValidator,
	MaxValueValidator,
)
from django.db import models

choices = (
	(1, 'House'),
	(2, 'Car'),
	(3, 'Light'),
	(4, 'Buzz'),
	(5, 'Year'),
	(10, 'Star Patrick'),
)


class Item(models.Model):

	item_id = models.AutoField(
		primary_key = True,
		db_column = 'ITEM_ID',
		verbose_name = 'ID',
	)
	item_name = models.CharField(
		max_length = 20,
		blank = True, 
		null = True,
		unique = True,
		db_column = 'ITEM_NAME',
		verbose_name = 'NAME',
	)
	item_image = models.ImageField(
		blank = True,
		null = True,
		upload_to = 'item/image/',
		db_column = 'ITEM_IMAGE',
		verbose_name = 'IMAGE',
	)
	item_bool = models.BooleanField(
		blank = True,
		null = True,
		db_column = 'ITEM_BOOL',
		verbose_name = 'BOOL',

	)
	item_date = models.DateField(
		blank = True,
		null = True,
		auto_now_add = True, # Date of creation.
		db_column = 'ITEM_DATE',
		verbose_name = 'DATE',
	)
	item_update_date = models.DateTimeField(
		blank = True,
		null = True,
		auto_now = True, # Updates the data at every change.
		db_column = 'ITEM_UPDATE_DATE',
		verbose_name = 'UPDATE_DATE',
	)
	item_decimal = models.DecimalField(
		blank = True,
		null = True,
		# 999,99 --> 1000,01 and 999,999 (not possible)
		max_digits = 5,
		decimal_places = 2,
		db_column = 'ITEM_DECIMAL',
		verbose_name = 'DECIMAL',
	)
	item_email = models.EmailField(
		blank = True,
		null = True,
		max_length = 254,
		db_column = 'ITEM_EMAIL',
		verbose_name = 'EMAIL',
	)
	item_file = models.FileField(
		blank = True,
		null = True,
		upload_to = 'item/file/',
		max_length = 254,
		db_column = 'ITEM_FILE',
		verbose_name = 'FILE',
	)
	item_integer = models.IntegerField( # Values from -2147483648 to 2147483647.
		blank = True,
		null = True,
		default = 1,
		validators = [
			MaxValueValidator(999),
			MinValueValidator(1),
		],
		db_column = 'ITEM_INTEGER',
		verbose_name = 'INTEGER',
	)
	item_slug = models.SlugField(
		blank = True,
		null = True,
		max_length = 60,
		db_column = 'ITEM_SLUG',
		verbose_name = 'SLUG',
	)
	item_name = models.TextField(
		blank = True, 
		null = True,
		db_column = 'ITEM_TEXT',
		verbose_name = 'TEXT',
	)
	item_url = models.URLField(
		blank = True,
		null = True,
		max_length = 200,
		db_column = 'ITEM_URL',
		verbose_name = 'URL',
	)
	item_uuid = models.UUIDField(
		blank = True,
		null = True,
		db_column = 'ITEM_UUID',
		verbose_name = 'UUID',
	)

	class Meta:

		db_table = 'ITEM'
		managed = True
		ordering = ['item_id']
		verbose_name = 'Item'
		verbose_name_plural = 'Items'

	def __str__(self):
		return self.item_name