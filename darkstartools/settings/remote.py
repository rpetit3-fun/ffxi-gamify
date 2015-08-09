from darkstartools.settings.common import *

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dspdb',
        'USER': 'darkstar',
        'PASSWORD': 'darkstar',
        'HOST': '25.154.139.241',
        'PORT': '3306',
    }
}
