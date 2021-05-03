from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from django.urls import path

urlpatterns = [
    url("",include("home.urls")),
    url('^social/', include('social_django.urls', namespace='social')),
    url("^account/", include("account.urls")),
    path('admin/', admin.site.urls),
    url("^questions/", include("QandA.urls")),
    url("^chatroom/", include("chatroom.urls")),
    url("^peers/", include("peer.urls")),
]
