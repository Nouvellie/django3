# -*- coding: utf-8 -*-
from __future__ import unicode_literals

''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "8.0" 
__created__     =       "01/16/2019 08:53" 
''' 


from django.db import models


class TestReact(models.Model):

	test_react_id = models.AutoField(
		primary_key = True,
		db_column = 'TEST_REACT_ID',
		verbose_name = 'ID',
	)
	test_react_title = models.CharField(
		max_length = 100,
		blank = True, 
		null = True,
		db_column = 'TEST_REACT_TITLE',
		verbose_name = 'TITLE',
	)
	test_react_description = models.CharField(
		max_length = 500,
		blank = True, 
		null = True,
		db_column = 'TEST_REACT_DESCRIPTION',
		verbose_name = 'DESCRIPTION',
	)
	test_react_image = models.ImageField(
		blank = True,
		null = True,
		upload_to = 'react_1/image/',
		db_column = 'TEST_REACT_IMAGE',
		verbose_name = 'IMAGE',
	)