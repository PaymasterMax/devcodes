from django.http import HttpResponse
from django.shortcuts import render

def handler500(request):
    return render(request , "devcodes500.html")


def handler404(request , error):
    print("Hello duncan. codethug\n\n\n")
    return HttpResponse("Hello world404")
