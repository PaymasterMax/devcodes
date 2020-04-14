from django.conf.urls import url
from . import views
app_name = "questions"

urlpatterns = [
    url("^$" , views.questionsview , name = "questions"),

]
