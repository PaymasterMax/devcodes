from django.shortcuts import render,redirect
from signup.models import Signup as signmod
from .models import ChatModel as chatmod
from django.db.models import Q


def inbox(request):
    try:
        userdetails = signmod.objects.get(username = request.session["username"])
        newmessage = chatmod.objects.filter(r2uid_id =  userdetails.uid, bell_seen = False).count()

    except Exception as e:
        request.session["redirect"] = "/chatroom/"
        return redirect("/login/")

    else:
        all_messages = chatmod.objects.filter(r2uid_id = userdetails.uid).order_by("-text_time")

        # test = chatmod.objects.filter(r2uid_id = )
        test = chatmod.objects.filter(r2uid_id = userdetails.uid).values("r1uid_id").distinct()
        print(test)
        return render(request , "chatroom/inbox.html" , context = {"all_messages":all_messages , "userdetails":userdetails , "newmessage":newmessage})


def chatrm(request , chat_user):
    try:
        userdetails = signmod.objects.get(username = request.session["username"])
        chats = chatmod.objects.filter(Q(r1uid_id = userdetails.uid , r2uid_id = chat_user) | Q(r1uid_id = chat_user , r2uid_id = userdetails.uid)).order_by("text_time")
        check_bell = chatmod.objects.filter(r2uid_id =  userdetails.uid, bell_seen = False)
        check_bell.update(bell_seen = True)
        ch_user = signmod.objects.get(uid = chat_user)

    except Exception as e:
        print(e)
        request.session["redirect"] = "/chatroom/{}/".format(chat_user)
        return redirect("/login/")

    else:
        return render(request , "chatroom/messages.html" , context = {"userdetails":userdetails , "chats":chats , "receiver":ch_user})


# update chats
def updatechats(request):
    if request.method == "POST":
        try:
            receiver = int(request.POST["re"])
            msg = request.POST["msg"]
            id = signmod.objects.get(username = request.session["username"]).uid

        except Exception as e:
            # request.session["redirect"] = "/chatroom/updatechats/"
            return redirect("/chatroom/{}/#frm".format(receiver))

        else:
            chatmod.objects.create(text_message = msg , r1uid_id = id, r2uid_id = receiver , bell_seen = False)
            return redirect("/chatroom/{}/#frm".format(receiver))
    else:
        pass
