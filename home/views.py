from django.shortcuts import render,redirect
from django.http import HttpResponse
from signup.models import Signup

def homeview(request):
    try:
        userlog = request.session["username"]
        userinfo = Signup.objects.get(username = userlog)
    except Exception as e:
        return redirect("/login/")

    else:
        userlog = True
        return render(request , "home/home.html" , context = {"userinfo":userinfo , "userlog":userlog})
