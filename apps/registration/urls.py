''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "7.0" 
__created__     =       "01/14/2019 16:21" 
''' 


from .views import SignUpView
from django.urls import path
 
 
urlpatterns = [ 
	path(
        'accounts/signup',
		SignUpView.as_view(),        
        name = "signup",
    ), 
] 