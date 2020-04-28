from django.contrib import admin
# from django.urls import path
from django.conf.urls import url , include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url('master/', admin.site.urls),
    url("^$" , include("home.urls")),
    url("login/" , include("login.urls")),
    url("signup/" , include("signup.urls")),
    url("profile/" , include("uprofile.urls")),
    url("codesnippet/" , include("codesnippet.urls")),
    url("questions/" , include("questions.urls")),
    url("peers/" , include("peer.urls")),
    url("chatroom/" , include("chatroom.urls")),
]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
