"""
Django settings for GroupB24 project.


Generated by 'django-admin startproject' using Django 4.1.dev20220210102451.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from pathlib import Path
import sys
import django_heroku
import os



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
#<<<<<<< HEAD
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xk)-_96=6fu!4kxi2+1id@!eb@qgarxd*t9#my@1hy)6ow*41@'

# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j8ml3&6am0u)7*otv*f+)&^0d%byauf=!1fm0lhwegca@oe^t_'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'bootstrap5',
    'WOMbasic.apps.WombasicConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # Add the following django-allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',  # for Google OAuth 2.0
    # ...
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'GroupB24.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ 'templates'],
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

WSGI_APPLICATION = 'GroupB24.wsgi.application'


# Database
#<<<<<<< HEAD
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
#=======
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
#>>>>>>> 8d4a8833ce2469efd874d353703b0fdc742f97df

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "d8ukhh84qk1vus",
        "USER": "qcvqxkceomdqbn",
        "PASSWORD": "d95eff4eb93adfe61e8d8b84f9d709d14e3cb7cb68b0784405577d9733c3f9a2",
        "HOST": "ec2-52-22-226-8.compute-1.amazonaws.com",
        "PORT": "5432",
        "TEST": {
            "NAME": "testdb",
        },
    }
}

if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'

# Password validation
#<<<<<<< HEAD
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
#=======
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
#>>>>>>> 8d4a8833ce2469efd874d353703b0fdc742f97df

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


# Internationalization
#<<<<<<< HEAD
# https://docs.djangoproject.com/en/3.2/topics/i18n/
#=======
# https://docs.djangoproject.com/en/dev/topics/i18n/
#>>>>>>> 8d4a8833ce2469efd874d353703b0fdc742f97df

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

#<<<<<<< HEAD
USE_L10N = True

#=======
#>>>>>>> 8d4a8833ce2469efd874d353703b0fdc742f97df
USE_TZ = True


# Static files (CSS, JavaScript, Images)
#<<<<<<< HEAD
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
#=======
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field
#>>>>>>> 8d4a8833ce2469efd874d353703b0fdc742f97df

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_heroku.settings(locals())

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]
SITE_ID = 2
LOGIN_REDIRECT_URL = '/'

# Additional configuration settings
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET= True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = '/media'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_FILES_DIRS = (
    os.path.join(BASE_DIR, 'static')
)

django_heroku.settings(locals(), test_runner=False)
