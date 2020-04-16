from django.shortcuts import render
# Create your views here.

def questionsview(request):
    return render(request , "questions/questions.html")


def answersview(request , Quid):
    return render(request , "questions/answers.html")
