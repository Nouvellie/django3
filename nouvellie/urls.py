''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "1.0" 
__created__     =       "12/06/2019 23:27" 
''' 


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
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

    # Apps. 
    path(
        '',
        include('apps.testmodels.urls'),
    ), 

    # Accounts.
    path(
        'accounts/',
        include('django.contrib.auth.urls'),
    ),
    path(
        'accounts/login',
        auth_views.LoginView.as_view(),
        name = 'login',
    ),
] + static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )