''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "1.0" 
__created__     =       "12/06/2019 23:27" 
''' 


from django.db import models


class Color(models.Model):


	color_id = models.AutoField(
		primary_key = True,
		db_column = 'COLOR_ID',
		verbose_name = 'ID',
	)
	color_name = models.CharField(
		max_length = 20,
		blank = True, 
		null = True,
		unique = True,
		db_column = 'COLOR_NAME',
		verbose_name = 'NAME',
	)

	class Meta:

		db_table = 'COLOR'
		managed = True
		ordering = ['color_id']
		verbose_name = 'Color'
		verbose_name_plural = 'Colors'

	def __str__(self):
		return self.color_name