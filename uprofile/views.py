from django.shortcuts import render,redirect
from django.http import HttpResponse
from chatroom.models import ChatModel as chtb
from django.contrib.auth.hashers import make_password
from signup.models import Signup as sp

def profileview(request):
    if request.method == "GET":
        try:
            mydetails = sp.objects.get(username = request.session['username'])
            newmessage = chtb.objects.filter(r2uid_id =  mydetails.uid, bell_seen = False).count()
        except Exception as e:
            request.session["redirect"] = "/profile/"
            return redirect("/login/")
        else:
            return render(request , "uprofile/uprofile.html" , context = {"mydetails":mydetails , "newmessage":newmessage})

def update_profile(request):
    if request.method == "POST":
        try:
            edit_user_details = sp.objects.get(username = request.session['username'])
            try:
                edit_user_details.profilepic=request.FILES["profile"]
            except Exception as e:
                pass
            edit_user_details.email = request.POST["email"]
            edit_user_details.username = request.POST["username"]
            edit_user_details.hobby = request.POST["language"].title()
            edit_user_details.save()
            request.session["username"] = request.POST["username"]
        except Exception as e:
            return redirect("/profile/")
        else:
            return redirect("/profile/")
    else:
        return redirect("/profile/")

def changepassword(request):
    try:
        print(request.session.keys())
        userinfo = sp.objects.get(username = request.session["username"])
    except Exception as e:
        return redirect("/login/")
    else:
        newpass = request.POST["password"]
        confirm = request.POST["confirmpassword"]
        if newpass ==confirm:
            userinfo.password = make_password(newpass)
            userinfo.save()
            return HttpResponse("Password changed ..")
        else:
            return HttpResponse("Password not changed.")
