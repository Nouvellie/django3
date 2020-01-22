''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "9.0" 
__created__     =       "01/17/2019 20:44" 
''' 


from .models import (
	Images,
	Mix,
	Testing,
)
from rest_framework import serializers


class ImagesSerializer(serializers.ModelSerializer):

	class Meta:

		model = Images
		fields = (
			'images_id',
			'images_url',
			'testing_id',
		)


class TestingSerializer(serializers.ModelSerializer):

	class Meta:

		model = Testing
		fields = (
			'testing_id',
			'testing_name',
		)

class MixSerializer(serializers.ModelSerializer):

	class Meta:

		model = Mix
		fields = (
			'mix_id',
			'images_id',
			'testing_id',
		)