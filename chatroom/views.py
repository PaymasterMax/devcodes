from django.shortcuts import render,redirect
from signup.models import Signup as signmod
from .models import ChatModel as chatmod
from django.db.models import Q


def chatrm(request , chat_user):
    try:
        userdetails = signmod.objects.get(username = request.session["username"])
        chats = chatmod.objects.filter(Q(r1uid_id = userdetails.uid , r2uid_id = chat_user) | Q(r1uid_id = chat_user , r2uid_id = userdetails.uid)).order_by("text_time")
        check_bell = chatmod.objects.filter(r2uid_id =  userdetails.uid, bell_seen = False)
        check_bell.update(bell_seen = True)

    except Exception as e:
        print(e)
        return redirect("/login/")

    else:
        return render(request , "chatroom/messages.html" , context = {"userdetails":userdetails , "chats":chats , "receiver":chat_user})


# update chats
def updatechats(request):
    if request.method == "POST":
        try:
            receiver = int(request.POST["re"])
            msg = request.POST["msg"]
            id = signmod.objects.get(username = request.session["username"]).uid

        except Exception as e:
            return redirect("/chatroom/{}/#frm".format(receiver))

        else:
            chatmod.objects.create(text_message = msg , r1uid_id = id, r2uid_id = receiver , bell_seen = False)
            return redirect("/chatroom/{}/#frm".format(receiver))
    else:
        pass
