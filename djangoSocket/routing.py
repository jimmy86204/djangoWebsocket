from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chatroom.routing

application = ProtocolTypeRouter({
  # (http->django views is added by default)
  'websocket': AuthMiddlewareStack(
    URLRouter(
      chatroom.routing.websocket_urlpatterns
    )
  ),
})