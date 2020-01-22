''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "1.0" 
__created__     =       "12/06/2019 23:27" 
''' 


from apps.react_1.views import (
    ItemViewSet,
    TestViewSet,
)
from apps.angular_2.views import (
    ImagesModelViewSet,
    MixModelViewSet,
    TestingModelViewSet,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/react_1/test', TestViewSet, 'react1_test')
router.register(r'api/react_1/model', ItemViewSet, 'react1_model')
router.register(r'api/angular_2/images', ImagesModelViewSet, 'angular2_images')
router.register(r'api/angular_2/testing', TestingModelViewSet, 'angular2_testing')
router.register(r'api/angular_2/mix', MixModelViewSet, 'angular2_mix')


# Every URL must end with slash.
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
    path(
        '',
        include('apps.registration.urls'),
    ), 
    path(
        'api/',
        include('apps.angular_1.urls'),
    ),
    path(
        'api/',
        include('apps.angular_2.urls'),
    ),  


    # Router:
    path(
        '',
        include(router.urls),
    ),

    # Accounts.
    path(
        'accounts/',
        include('django.contrib.auth.urls'),
    ),
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(),
        name = 'login',
    ),
] + static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )