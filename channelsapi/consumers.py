from channels.consumer import AsyncConsumer


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self , event):
        print("Hellow \n\n\n\n")
        self.send({
            "type":"websocket.accept",
        })

    async def websocket_receive(self , event):
        pass

    async def websocket_disconnect(self , event):
        pass
