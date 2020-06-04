from django.http import HttpResponse
from django.shortcuts import render

def handler500(request):
    return render(request , "bugs/devcodes500.html")


def handler404(request , exception):
    return render(request , "bugs/devcodes404.html")
