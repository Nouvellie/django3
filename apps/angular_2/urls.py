''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "9.0" 
__created__     =       "01/17/2019 20:44" 
'''


from .views import (
	ImagesView,
	MixPutView,
)
from django.urls import path


urlpatterns = [
	path(
        'angular_2/home',
        ImagesView.as_view(),
        name = "angular_2_images",
    ), 
    path(
        'angular_2/mixput',
        MixPutView.as_view(),
        name = "angular2_mixput",
    ),
]