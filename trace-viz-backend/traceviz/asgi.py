"""
ASGI config for traceviz project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import mainapp.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'traceviz.settings')

asgi_application = get_asgi_application()


application = ProtocolTypeRouter({
"http": asgi_application,
"websocket": 
    AuthMiddlewareStack(
            URLRouter(mainapp.routing.websocket_urlpatterns) 
    ),
})
