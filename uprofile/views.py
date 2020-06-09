from django.shortcuts import render,redirect
from django.http import HttpResponse
from chatroom.models import ChatModel as chtb
from django.contrib.auth.hashers import make_password
from signup.models import Signup as sp
import json
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
                print(f"{e}\n\n\n\n\n")
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
    logger = False
    try:
        userinfo = sp.objects.get(username = request.session["username"])
    except Exception as e:
        return redirect("/login/")
    else:
        newpass = request.POST["password"]
        confirm = request.POST["confirmpassword"]
        if newpass ==confirm:
            userinfo.password = make_password(newpass)
            userinfo.save()
            password_status = "Password changed sucessfully."
            logger = True
        else:
            password_status = "Pasword not changed. Please try again"
            logger = False

        logger = json.dumps({"logger":True,"password_status":password_status})
        return HttpResponse(logger , content_type = "application/json")
