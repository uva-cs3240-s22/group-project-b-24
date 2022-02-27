"""
ASGI config for GroupB24 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/
>>>>>>> 8d4a8833ce2469efd874d353703b0fdc742f97df
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GroupB24.settings')

application = get_asgi_application()
