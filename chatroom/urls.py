from django.conf.urls import url
from . import views

app_name = "chatroom"

urlpatterns = [
    url("^$" , views.inbox , name = "inbox"),
    url("^updatemessage/" , views.updatemessage , name = "updatemessage"),
    url("^check_new_message/" , views.check_new_message , name = "check_new_message"),
    url("^adminpanel/$" , views.adminpanel , name = "adminpanel"),
    url("^(?P<chat_user>[\d]+)/$" , views.chatrm , name = "chatroom"),
    url("^updatechats/$" , views.updatechats , name = "updatechats"),
    url("^delete/(?P<chtid>[\d]+)/(?P<chat_user>[\d]+)/$" , views.deletechat , name = "delete")
]
