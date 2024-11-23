"""
tres eventos: connect, recive, disconect
"""
import json
from channels.generic.websocket import WebsocketConsumer 
from asgiref.sync import async_to_sync
from django.utils import timezone


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.id_sala = self.scope['url_route']['kwargs']['id_sala']
        self.id = self.scope['url_route']['kwargs']['id_sala']

        self.room_group_name = "sala_chat_%s" % self.id

        self.user = self.scope['user']

        print("MI IDDD MI IDDDDDDDDDDDDDDDDDDDD")
        print("conexion establecida al room group name" + self.room_group_name)
        print("CHANNEL NAME DEL USUARIO o: ")
        print("conexion establecida channel name " + self.channel_name)

        # con estos dos parametros me conecto al web socket ooo
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)

        # print(f"Conexión a la sala: {self.id_sala}")
        self.accept()
    
    def disconnect(self, close_code):
        print("desconectado------------------------------")
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)
        

    def receive(self, text_data):
        print("mensaje captado")

        try:
            # Cambiar de json.load() a json.loads()
            text_data_json = json.loads(text_data)
            message = text_data_json["message"]

            # id del usuario que envia el mensaje 
            if self.scope['user'].is_authenticated:
                sender_id = self.scope['user'].id
            else:
                sender_id = None
            
            if sender_id:
                # mandar a la base de datos el mensaje
                async_to_sync(self.channel_layer.group_send)(self.room_group_name, {
                    "type": "chat_message", 
                    "message": message,
                    "username": self.user.username,
                    'datetime': timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S'),
                    'sender_id': sender_id,
                    "prioridad": "baja",
                    "personas": []
                })
            else:
                print("usuario no autenticado") 

        except json.JSONDecodeError as e:
            print("error al procesar el mensaje JSON:", e)


    def chat_message(self, event):
        message = event['message']
        username = event['username']
        datetime = event['datetime']
        sender_id = event['sender_id']
        prioridad = event['prioridad']
        personas = event['personas']

        current_user_id = self.scope['user'].id
        if sender_id != current_user_id:
            self.send(text_data=json.dumps({
                'message':message,
                'username': username,
                'datetime': datetime,
                "prioridad": prioridad,   
                'personas': personas 
            }))
