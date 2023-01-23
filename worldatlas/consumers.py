import json
from asgiref.sync import asyncio, sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from worldatlas.models import Room

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user = self.scope['user']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        #room_turn = await self.get_room_turn(self.room_name)
        #await self.send(text_data=json.dumps({
        #    'type': 'connection_established',
        #    'message': room_turn,
        #    'username': self.user.username,
        #    'room': self.room_name,
        #}))

    async def disconnect(self, close_code):
        room_name = self.scope['url_route']['kwargs']['room_name']
        await self.delete_room(room_name)
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username, 
                'room': room,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room 
        }))

    @sync_to_async
    def delete_room(self, room):
        room = Room.objects.get(slug=room)
        room.delete()

    @sync_to_async
    def get_room_turn(self, room):
        room = Room.objects.get(name=room)
        return room.first_turn
