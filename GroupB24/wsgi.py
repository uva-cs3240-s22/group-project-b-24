"""
WSGI config for GroupB24 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
>>>>>>> 8d4a8833ce2469efd874d353703b0fdc742f97df
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GroupB24.settings')

application = get_wsgi_application()
