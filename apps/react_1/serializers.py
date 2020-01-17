''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "8.0" 
__created__     =       "01/16/2019 08:53" 
''' 


from .models import TestReact
from rest_framework import serializers


class TestReactSerializer(serializers.ModelSerializer):


	class Meta:

		model = TestReact
		fields = (
			'test_react_id',
			'test_react_title',
			'test_react_description',
			'test_react_image',
		)