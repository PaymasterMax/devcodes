from django.conf.urls import url
from . import views
app_name = "home"

urlpatterns = [
    url("^$" , views.homeview , name = "home"),
    url("^Policies/" , views.Policies , name = "Policies"),
]
