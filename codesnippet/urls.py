from django.conf.urls import url
from . import views
app_name = "codesnippets"

urlpatterns = [
    url("^$" , views.codeview , name = "codesnippets"),

]
