from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User 
from .models import Message


import json

class ChatConsumer(SyncConsumer):

    def websocket_connect(self, event):

        sender_user = self.scope['url_route']['kwargs']['sendername']
        reciever_user = self.scope['url_route']['kwargs']['recievername']
        uid = sender_user + reciever_user

      
      
        self.room_name = "".join(sorted(uid))
        print("".join(sorted(uid)))

        async_to_sync(self.channel_layer.group_add)(
             self.room_name, self.channel_name)

        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        print(event)

        message = json.dumps({
            'thread': event["text"],
            'sender': self.scope['url_route']['kwargs']['sendername']
        })

        print(self)

        self.store_msg(event["text"])

        async_to_sync(self.channel_layer.group_send)( self.room_name,
                                                     {
                                                         "type": "websocket.message",
                                                         "text": message,
                                                     }

                                                     )

    def websocket_message(self, event):
        self.send({
            "type": "websocket.send",
            "text": event["text"],
        })

    def websocket_disconnect(self, event):
        print("disconnected ")
        async_to_sync(self.channel_layer.group_discard)(
            'broadcast', self.channel_name)

    def store_msg(self, text):
        Message.objects.create(thread=self.room_name, sender=self.scope['url_route']['kwargs']['sendername'], text=text)
        
