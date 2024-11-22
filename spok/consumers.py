"""
tres eventos: connect, recive, disconect
"""
import json
from channels.generic.websocket import WebsocketConsumer 


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.id_sala = self.scope['url_route']['kwargs']['id_sala']
        print(f"Conexión a la sala: {self.id_sala}")
        self.accept()
    
    def disconnect(self, close_code):
        print("desconectado------------------------------")
        pass

    def receive(self, text_data):
        print("mendaje captado")
        try:
            # convierto para manejarlo mejor 
            text_data_json = json.load(text_data)
            # pasar por el texta data la hora de enc¿vio (luego)
            message = text_data_json["message"]

            # definido el consumer 
            self.send(text_data = json.dumps({
                "message" : message
            }))
        except json.JSONDecodeError as e:
            print("error")

