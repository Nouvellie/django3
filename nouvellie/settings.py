''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "1.0" 
__created__     =       "12/06/2019 23:27" 
''' 


import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'u1sut*fwo+@a(_a!rd9lf*-pc)#@1p#20blnh@(9_l480&0c*j'

'''
CREDENTIALS:

USERNAME = nouvellie
PASSWORD = testing3341
'''

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Main:
    'apps.core',

    # Apps.
    'apps.angular_1',
    'apps.angular_2',
    'apps.react_1',
    'apps.registration',
    'apps.testmodels',

    # DRF.
    'rest_framework',

    # Supports.
    'corsheaders',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', 
    )
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = 'http://localhost:3000',

ROOT_URLCONF = 'nouvellie.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nouvellie.wsgi.application'

# DATABASES = { 
#     'default': { 
#         'ENGINE':       'django.db.backends.mysql', 
#         'NAME':         'nouvellie', 
#         'PORT':         '3306', 
#         'USER':         'nouvellie', 
#         'PASSWORD':     'testing3341', 
#         'HOST':         '127.0.0.1', 
#     }, 
# } 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

''' 
MYSQL USER CREATION (LOCALHOST):

CREATE USER 'nouvellie'@'%' identified by 'testing3341';
ALTER USER 'nouvellie'@'%' identified WITH mysql_native_password by 'testing3341';
GRANT ALL PRIVILEGES ON *.* to 'nouvellie'@'%';

Fix migration errors.
python3 manage.py makemigrations
python3 manage.py makemigrations *
python3 manage.py migrate --fake core zero
python3 manage.py makemigrations *
python3 manage.py migrate --fake-initial
'''
 
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') 

MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'