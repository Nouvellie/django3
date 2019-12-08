''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "1.0" 
__created__     =       "12/06/2019 23:27" 
''' 


from django.core.asgi import get_asgi_application


import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nouvellie.settings')

application = get_asgi_application()