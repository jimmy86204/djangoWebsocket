from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

import json
import logging

# logging module with django logging
logger = logging.getLogger('django')

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # get name from ws url args
        self.name = self.scope['url_route']['kwargs']['name']
        logger.debug('connect')
        # Join group group_add('group_name', 'channel_name')
        async_to_sync(self.channel_layer.group_add)(
            'lobby',
            self.channel_name
        )

        self.accept()
        self.group_send(f'{self.name} join the room.')

    def disconnect(self, close_code):
        # Leave group group_discard('group_name', 'channel_name')
        async_to_sync(self.channel_layer.group_discard)(
            'lobby',
            self.channel_name
        )
        self.group_send(f'{self.name} left the room.')
        

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = self.name + ': ' + text_data_json['message']
        logger.debug('send')

        # Send message to room group
        self.group_send(message)

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    def group_send(self, msg, group='lobby', type_='chat_message'):
        # group_send('group_name', {'type': type, **kwargs})
        # type means what function you want to do
        async_to_sync(self.channel_layer.group_send)(
            group,
            {
                'type': type_,
                'message': msg
            }
        )