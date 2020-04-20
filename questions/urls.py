from django.conf.urls import url
from . import views
app_name = "questions"

urlpatterns = [
    url("^$" , views.questionsview , name = "questions"),
    url("^updateanswers/(?P<Qid>[\d]+)/$" , views.update_answers , name = "updateanswers"),
    url("^answers/(?P<Qid>[\d]+)/$" , views.answersview , name = "answers"),
    url("^updatequestions/(?P<Qid>[\d]+)/$" , views.askquestionsview , name = "askquestions"),
]
