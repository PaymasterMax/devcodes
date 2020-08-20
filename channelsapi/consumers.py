from channels.consumer import AsyncConsumer


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self , event):
        print("Hellow \n\n\n\n")
        await self.send({
            "type":"websocket.accept",
        })

    async def websocket_receive(self , event):
        await self.send({
            "type":"websocket.send",
            "text":"Hello world",
        })

    async def websocket_disconnect(self , event):
        await self.send({
            "type":"websocket.close",
        })
