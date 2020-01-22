''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "7.0" 
__created__     =       "01/15/2019 10:32" 
''' 


from django.db import models


class TestAngular(models.Model):

	test_angular_id = models.AutoField(
		primary_key = True,
		db_column = 'TEST_ANGULAR_ID',
		verbose_name = 'ID',
	)
	test_angular_text = models.CharField(
		max_length = 200,
		blank = True, 
		null = True,
		db_column = 'TEST_ANGULAR_TEXT',
		verbose_name = 'TEXT',
	)
	test_angular_bool = models.BooleanField(
		blank = True,
		null = True,
		db_column = 'TEST_ANGULAR_BOOL',
		verbose_name = 'BOOL',
	)