from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def codeview(request):
    return render(request , "codesnippet/codesnipps.html")
