from django.shortcuts import render , redirect
from signup.models import Signup
from .forms import anserform
from django.db.models import Count
from .models import Questions , Answers , QuestionLike as qlike
from chatroom.models import ChatModel as chtb
from chatroom.models import FeedBack as fd
from django.http import JsonResponse , HttpResponse

def questionsview(request):
    all_questions = Questions.objects.all().annotate(no_of_answers = Count("question_to_answer")).order_by("-time_posted")
    try:
        userdetails = Signup.objects.get(username = request.session["username"])
        newmessage = chtb.objects.filter(r2uid_id =  userdetails.uid, bell_seen = False).count()
        userlog = True
    except Exception as e:
        userlog = False
        request.session["redirect"] = "/questions/"
        return redirect("/login/")
        return render(request , "questions/questions.html" , context = {"Questions":all_questions , "userlog":userlog})

    else:
        return render(request , "questions/questions.html" , context = {"Questions":all_questions , "mydetails":userdetails , "newmessage":newmessage , "userlog":userlog})
