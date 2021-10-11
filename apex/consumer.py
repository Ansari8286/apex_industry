# channels              2.4.0
# channels-redis        2.4.2

import datetime
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import *
# this is admin notification system

class AlertSystem(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status':'connected from django channels'}))

    #{'user_id':1, 'message':'hi'} thats how we'll send data from front end
    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type': 'run',
                'payload': text_data
            }
        )
    def disconnect(self, *args , **kwargs):
        print('Alert System disconnected')

    def send_notification(self, event):
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({'payload':data}))


class UserAlert(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = "room_%s" % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        try:
            reg = Register.give_noti_detail(self.room_name)
            self.accept()
            # self.send(text_data=json.dumps({'payload':reg}))
        except:
            # print(reg)
            self.accept()
            self.send(text_data=json.dumps({'payload':'connected from django channels user alert'}))
    def receive(self,text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'send_alert_user',
                'payload': text_data
            }
        )

    def disconnect(self,close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def send_alert_user(self, event):
        try:
            data = json.loads(event.get('value'))
            self.send(text_data=json.dumps({'payload':data}))
        except:
            pass