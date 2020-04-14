from django.shortcuts import render
# Create your views here.

def questionsview(request):
    return render(request , "questions/questions.html")
