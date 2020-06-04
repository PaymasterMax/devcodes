from django.conf.urls import url
from . import views
app_name = "profile"

urlpatterns = [
    url("^$" , views.profileview , name = "profile"),
    url("^update/" , views.update_profile , name = "update"),
    url( "^changepassword/$" , views.changepassword , name = "changepassword"),
]
