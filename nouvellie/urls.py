''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "1.0" 
__created__     =       "12/06/2019 23:27" 
''' 


from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/',		 	admin.site.urls),
]