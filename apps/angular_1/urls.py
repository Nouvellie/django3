''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "7.0" 
__created__     =       "01/15/2019 10:32" 
''' 


from .views import (
    TestAngularDetailView,
	TestAngularListView,
	TestView,
)
from django.urls import path


urlpatterns = [ 
	path(
        'test/',
        TestView.as_view(),
        name = "angular1_test",
    ),
    path(
        'angular_1/',
        TestAngularListView.as_view(),
        name = "angular1_list",
    ),
    path(
        'angular_1/<int:pk>/',
        TestAngularDetailView.as_view(),
        name = "angular1_detail",
    ),
]