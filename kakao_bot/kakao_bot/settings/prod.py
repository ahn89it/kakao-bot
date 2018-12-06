from .common import *

INSTALLED_APPS += ['storages']

STATICFILES_STORAGE = 'askdjango.storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'askdjagno.storages.MediaStorage'

AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME')
AZURE_ACCOUNT_KEY  = os.environ.get('AZURE_ACCOUNT_KEY')
AZURE_SSL = True

DATABASES ={
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'HOST' : os.environ.get('DB_HOST'),
        'NAME' : os.environ.get('DB_NAME'),
        'USER' : os.environ.get('DB_USER'),
        'PASSWORD' : os.environ.get('DB_PASSWORD'),
        'OPTIONS' : {
            'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}