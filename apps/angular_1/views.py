''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "7.0" 
__created__     =       "01/15/2019 10:32" 
''' 


from .models import TestAngular
from .serializers import TestAngularSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
	get_object_or_404,
	render,
)
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_204_NO_CONTENT,
	HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView


class TestView(TemplateView):

	template_name = 'angular_1/test.html'


@method_decorator(login_required, name = 'dispatch')
class TestAngularListView(APIView):

	permission_classes = (AllowAny,)


	def get(self, request):
		
		test_angular_objects = TestAngular.objects.all()
		serializer = TestAngularSerializer(
						 test_angular_objects, 
						 many = True,
					 )
		return Response(serializer.data)


	@csrf_exempt
	def put(self, request):
		serializer = TestAngularSerializer(
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


@method_decorator(login_required, name = 'dispatch')
class TestAngularDetailView(APIView):

	permission_classes = (AllowAny,)


	def get(self, request, pk):
		test_angular_objects = get_object_or_404(TestAngular, pk = pk)
		serializer = TestAngularSerializer(test_angular_objects)
		return Response(serializer.data)


	def delete(self, request, pk):

		'''
		WARNING:
			Delete can not be used after an item is created,
			because the testAngularList is not updated at the same time.
		'''
		test_angular_objects = get_object_or_404(TestAngular, pk = pk)
		test_angular_objects.delete()
		return Response(status = HTTP_204_NO_CONTENT)
