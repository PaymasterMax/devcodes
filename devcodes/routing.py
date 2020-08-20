from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from channelsapi import consumers
from django.conf.urls import url

application = ProtocolTypeRouter({
                "websocket":AuthMiddlewareStack(
                        URLRouter([
                                url("/" , consumers.ChatConsumer),
                            ])
                )
})
