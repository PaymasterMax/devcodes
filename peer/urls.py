from django.conf.urls import url
from . import views

app_name = "peers"

urlpatterns = [
    url("^$" , views.peers , name = "peers"),
    url("locatepeers/" , views.locatepeers , name="locatepeers")
]
