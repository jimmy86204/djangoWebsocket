from django.urls import path, re_path
from chatroom.views import ChatRoom

app_name = 'chatroom'

urlpatterns = [
  path('', ChatRoom.as_view(), name='char_room'),
]