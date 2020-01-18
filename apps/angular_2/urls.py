''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "9.0" 
__created__     =       "01/17/2019 20:44" 
'''


from .views import ImagesView
from django.urls import path


urlpatterns = [
	path(
        'images',
        ImagesView.as_view(),
        name = "angular_2_images",
    ), 
]