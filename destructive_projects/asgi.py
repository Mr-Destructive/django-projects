import os
import django
django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'destructive_projects.settings')
from django.urls import re_path
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from worldatlas import consumers, routing

#application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    "websocket":AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    )
})
