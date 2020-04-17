from django.shortcuts import render
from signup.models import signup
# Create your views here.

def questionsview(request):
    return render(request , "questions/questions.html")


def answersview(request , Qid):
    try:
        userdetails = signup.objects.get(username = request.session["username"])
    except Exception as e:
        return render(request , "questions/answers.html" , context = {"userdetails":"userdetails"})
    else:
        return render(request , "questions/answers.html" , context = {"userdetails":userdetails})
