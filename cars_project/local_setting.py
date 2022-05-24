# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n46h&wbyrb0#blx7zjv=ji&_kz!sud)0h%spf$!ey3jgkjh)v@'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}
