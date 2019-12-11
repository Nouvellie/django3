''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "1.0" 
__created__     =       "12/06/2019 23:27" 
''' 


from django.contrib import admin
from django.urls import include, path


urlpatterns = [ 
 
    # Admin app. 
    path(
        'nouvellie-admin/',
        admin.site.urls,
    ), 

    # Main app. 
    path(
        '',
        include('apps.core.urls'),
    ), 

    # Accounts.
    path(
        '',
        include('apps.registration.urls'),
    ), 
] 