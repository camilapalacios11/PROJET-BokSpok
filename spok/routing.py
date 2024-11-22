from django.urls import path, re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'^ws/mostrar_sala/(?P<id_sala>\w+)/$', ChatConsumer.as_asgi()),
]