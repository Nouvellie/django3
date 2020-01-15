''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "7.0" 
__created__     =       "01/15/2019 10:32" 
''' 


from .views import TestView
from django.urls import path


urlpatterns = [ 
	path(
        'test',
        TestView.as_view(),
        name = "test",
    ),

]