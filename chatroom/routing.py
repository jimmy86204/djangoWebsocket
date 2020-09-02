from django.urls import re_path
from chatroom import consumers

websocket_urlpatterns = [
  re_path(r'^ws/chat/(?P<name>[^/]+)/$', consumers.ChatConsumer),
]