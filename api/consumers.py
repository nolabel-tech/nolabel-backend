import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            self.unique_id = self.scope['url_route']['kwargs']['unique_id']
            self.room_group_name = f'chat_{self.unique_id}'

            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            await self.accept()
        except Exception as e:
            await self.close()
            print(f'Error in connecting: {e}')

    async def disconnect(self, close_code):
        try:
            if hasattr(self, 'room_group_name'):
                # Leave room group
                await self.channel_layer.group_discard(
                    self.room_group_name,
                    self.channel_name
                )
        except Exception as e:
            print(f'Error in disconnecting: {e}')

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
            print(f'Received message: {message}')  # Логирование полученного сообщения

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )
        except Exception as e:
            print(f'Error in receiving message: {e}')

    async def chat_message(self, event):
        try:
            message = event['message']
            print(f'Broadcasting message: {message}')  # Логирование сообщения перед отправкой

            # Send message to WebSocket
            await self.send(text_data=json.dumps({
                'type': 'message',
                'message': message
            }))
        except Exception as e:
            print(f'Error in chat message: {e}')
