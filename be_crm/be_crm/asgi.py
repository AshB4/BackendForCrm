"""
ASGI config for be_crm project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'be_crm.settings')

application = get_asgi_application()

#allows python to talk to webserver
# Stands for Asynchronous Server Gateway Interface.
# Entry point for ASGI-compatible web servers to serve your Django application asynchronously.
# Used for running Django applications with asynchronous features, such as Django Channels for handling WebSockets and other async tasks.
# Responsible for setting up the ASGI application instance.
# wsgi.py:
