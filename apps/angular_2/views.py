# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
from .serializers import (
	ImagesSerializer,
	MixSerializer,
	TestingSerializer,
)
from django.shortcuts import (
	get_object_or_404,
	render,
)
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
	ListView,
	TemplateView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_204_NO_CONTENT,
	HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView
from rest_framework.viewsets import (
	ModelViewSet,
	ViewSet,
)

class ImagesModelViewSet(ModelViewSet):

	permission_classes = (AllowAny,)
	queryset = Images.objects.all()
	serializer_class = ImagesSerializer


class MixModelViewSet(ModelViewSet):

	permission_classes = (AllowAny,)
	queryset = Mix.objects.all()
	serializer_class = MixSerializer
	

class TestingModelViewSet(ModelViewSet):

	permission_classes = (AllowAny,)
	queryset = Testing.objects.all()
	serializer_class = TestingSerializer



class MixPutView(APIView):
	
	permission_classes = (AllowAny,)

	
	def get(self, request, images_id):
		
		test_angular_objects = get_object_or_404(Mix, images_id = images_id)
		serializer = MixSerializer(
						 test_angular_objects, 
						 # many = True,
					 )
		return Response(serializer.data)


	# @csrf_exempt
	def put(self, request, images_id):
		serializer = MixSerializer(
						 data = request.data,
					 )
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			Response(
				serializer.errors,
				status = HTTP_400_BAD_REQUEST,
			)

	def patch(self, request, images_id):
		mix_patch = Mix.objects.get(images_id = images_id)
		testing_object = Testing.objects.get(testing_id = request.data['testing_id'])
		mix_patch.testing_id = testing_object
		mix_patch.save()
		return Response(status = HTTP_204_NO_CONTENT)


class ImagesView(ListView):

	context_object_name = 'images'
	model = Images
	paginate_by = 1
	template_name = 'angular_2/images.html'

	def get_context_data(self, **kwargs):

		context = super(ImagesView, self).get_context_data(**kwargs)
		# # try:
		# #     page                = self.request.GET.dict()['page']
		# # except:
		# #     page                = 1
		# # context['diag']         = DiagDict.objects.values().filter(diag_dict_id=page)
		# # diag_image              = context['diag'][0]['images_id_id']
		# try:
		# 	pagemix = int(self.request.GET.dict()['page'])
		# 	try:
		# 		context['mixs'] = Mix.objects.get(images_id = pagemix)
		# 		print(context['mixs'])
		# 		context['putmix'] = False 
		# 	except:
		# 		context['putmix'] = True
		# except Exception as e:
		# 	print(e.args)
		# 	context['mixs'] = Mix.objects.first()
		# 	print(context['mixs'])
		# 	pass
		
		# print(context['mixs'])
		context['testing'] = Testing.objects.all()
		return context


class TestingView(TemplateView):

	template_name = 'angular_2/testing.html'