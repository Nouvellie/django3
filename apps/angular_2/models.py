''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "9.0" 
__created__     =       "01/17/2019 20:44" 
'''  


from django.db import models


class Images(models.Model):

	images_id = models.AutoField(
		primary_key = True,
		db_column = 'IMAGES_ID',
		verbose_name = 'IMAGES_ID',
	)
	images_url = models.URLField(
		max_length = 800,
		blank = True,
		null = True,
		db_column = 'IMAGES_URL',
		verbose_name = 'URL',
	)

	testing_id = models.ForeignKey(
		'Testing',
		blank = True,
		null = True,
		on_delete = models.DO_NOTHING,
		db_column = 'TESTING_ID',
		verbose_name = 'TESTING_ID',
	)

	def __str__(self):
		return self.images_url


class Testing(models.Model):

	testing_id = models.AutoField(
		primary_key = True,
		db_column = 'TESTING_ID',
		verbose_name = 'TESTING_ID',
	)
	testing_name = models.TextField(
		blank = True,
		null = True,
		db_column = 'TESTING_NAME',
		verbose_name = 'NAME',
	)

	def __str__(self):
		return self.testing_name


class Mix(models.Model):

	mix_id = models.AutoField(
		primary_key = True,
		db_column = 'MIX_ID',
		verbose_name = 'MIX_ID',
	)

	testing_id = models.ForeignKey(
		'Testing',
		blank = True,
		null = True,
		on_delete = models.DO_NOTHING,
		db_column = 'TESTING_ID',
		verbose_name = 'TESTING_ID',
	)
	images_id = models.ForeignKey(
		'Images',
		blank = True,
		null = True,
		on_delete = models.DO_NOTHING,
		db_column = 'IMAGES_ID',
		verbose_name = 'IMAGES_ID',
	)