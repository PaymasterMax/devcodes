from django.conf.urls import url
from . import views

app_name = "chatroom"

urlpatterns = [
    url("^(?P<chat_user>[\d]+)/$" , views.chatrm , name = "chatroom"),
    url("^updatechats/$" , views.updatechats , name = "updatechats"),
]
