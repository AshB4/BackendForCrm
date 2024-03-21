"""
WSGI config for be_crm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'be_crm.settings')

application = get_wsgi_application()

#allows python to talk to the web server
# Stands for Web Server Gateway Interface.
# Entry point for WSGI-compatible web servers to serve your Django application.
# WSGI is the traditional way of serving Python web applications.
# It provides a simple and universal interface between web servers and web applications/frameworks.
# Responsible for setting up the WSGI application instance.
