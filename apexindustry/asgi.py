"""
ASGI config for apexindustries project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
import os
import channels
import django
from channels.http import AsgiHandler

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
# from django.core.asgi import get_asgi_application

from apex.consumer import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apexindustry.settings')
# django.setup()  
application = get_asgi_application()

ws_patterns = [
    path('ws/alert/', AlertSystem),
    path('ws/user-alert/<room_code>/', UserAlert)
]

application = ProtocolTypeRouter({
    # "http": get_asgi_application(), 
    'websocket' : AuthMiddlewareStack(URLRouter(ws_patterns)),
})
