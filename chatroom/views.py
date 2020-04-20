from django.shortcuts import render,redirect
from signup.models import Signup as signmod
from .models import ChatModel as chatmod
from django.db.models import Q
# from django.db.models import aggregate


def chatrm(request , chat_user):
    try:
        userdetails = signmod.objects.get(username = request.session["username"])
        chats = chatmod.objects.filter(Q(r1uid_id = userdetails.uid , r2uid_id = chat_user) | Q(r1uid_id = chat_user , r2uid_id = userdetails.uid))
        # annotate(time_lapse = aggregate(text_time-1000))

    except Exception as e:
        print(e)
        return redirect("/login/")

    else:
        return render(request , "chatroom/messages.html" , context = {"userdetails":userdetails , "chats":chats , "receiver":chat_user})


def updatechats(request):
    if request.method == "POST":
        try:
            receiver = int(request.POST["re"])
            msg = request.POST["msg"]
            id = signmod.objects.get(username = request.session["username"]).uid

        except Exception as e:
            return redirect("/chatroom/{}/".format(receiver))

        else:
            chatmod.objects.create(text_message = msg , r1uid_id = id, r2uid_id = receiver)
            return redirect("/chatroom/{}/".format(receiver))
    else:
        pass
