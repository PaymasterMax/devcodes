from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from signup.models import signup

def profileview(request):
    if request.method == "GET":
        try:
            mydetails = signup.objects.get(username = request.session['username'])

        except Exception as e:
            return redirect("/login/")

        else:
            return render(request , "uprofile/uprofile.html" , context = {"mydetails":mydetails })

    else:
        pass



def update_profile(request):
    print(request.POST["username"])
    if request.method == "POST":
        try:
            edit_user_details = signup.objects.get(username = request.session['username'])
            edit_user_details.username = request.POST["username"]
            edit_user_details.pnumber = request.POST["phone"]
            edit_user_details.email = request.POST["email"]
            edit_user_details.hobby = request.POST["language"]
            edit_user_details.profilepic = request.FILES["profile"]
            edit_user_details.save()

        except Exception as e:
            return redirect("/profile/")

        else:
            return redirect("/profile/")

    else:
        return redirect("/profile/")


def peerview(request):
    return render(request , "uprofile/peers.html")
