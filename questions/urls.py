from django.conf.urls import url
from . import views
app_name = "questions"

urlpatterns = [
    url("^$" , views.questionsview , name = "questions"),
    # url("^feedback/$" , views.feed , name = "feedback"),
    # url("^updatelikes/$" , views.updatelikes , name = "updatelikes"),
    # url("^myquestions/$" , views.myquestions , name = "myquestions"),
    # url("^updateanswers/(?P<Qid>[\d]+)/$" , views.update_answers , name = "updateanswers"),
    # url("^answers/(?P<Qid>[\d]+)/$" , views.answersview , name = "answers"),
    # url("^updatequestions/$" , views.askquestionsview , name = "askquestions"),
]
