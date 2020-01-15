''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "7.0" 
__created__     =       "01/15/2019 10:32" 
''' 


from .models import TestAngular
from rest_framework import serializers


class TestAngularSerializer(serializers.ModelSerializer):


	class Meta:

		model = TestAngular
		fields = (
			'test_angular_id',
			'test_angular_text',
			'test_angular_bool',
		)