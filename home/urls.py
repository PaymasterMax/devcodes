from django.conf.urls import url
from . import views
app_name = "home"

urlpatterns = [
    url("^$" , views.homeview , name = "home"),
    url("^adminpanel/" , views.adminpanel , name = "adminpanel"),
]
