''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "7.0" 
__created__     =       "01/15/2019 10:32" 
''' 


from django.shortcuts import render
from django.views.generic import TemplateView


class TestView(TemplateView):

	template_name = 'angular/test.html'