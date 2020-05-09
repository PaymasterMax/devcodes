from django.contrib import admin
# from django.urls import path
# from django.conf.urls import handler404
from django.conf.urls import url , include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url('master/', admin.site.urls),
    url("^$" , include("home.urls")),
    url("login/" , include("login.urls")),
    url("signup/" , include("signup.urls")),
    url("profile/" , include("uprofile.urls")),
    url("questions/" , include("questions.urls")),
    url("peers/" , include("peer.urls")),
    url("chatroom/" , include("chatroom.urls")),
        # url(r'^oauth/', include('social_django.urls', namespace='social')),
]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


handler404 = views.handler404

handler500 = views.handler500
