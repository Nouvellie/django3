''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "4.0" 
__created__     =       "12/18/2019 08:50" 
''' 


from django.db import models


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
	item_image = ImageField(
		
	)

	class Meta:

		db_table = 'ITEM'
		managed = True
		ordering = ['item_id']
		verbose_name = 'Item'
		verbose_name_plural = 'Items'

	def __str__(self):
		return self.item_name