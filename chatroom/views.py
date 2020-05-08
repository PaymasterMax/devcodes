from django.shortcuts import render,redirect
from signup.models import Signup as signmod
from .models import ChatModel as chatmod , FeedBack as fd
from django.db.models import Q,Max

def db_unique(db_obj):
    unique_chat = list()
    for x in db_obj:
        x1 , x2 = x.r1uid_id , x.r2uid_id
        if x.r1uid_id in [value.r1uid_id for value in unique_chat]:
            if x.r2uid_id==x2:
                pass
            else:
                unique_chat.append(x)
        else:
            if x.r2uid_id in [value.r2uid_id for value in unique_chat]:
                if x.r1uid_id==x1:
                    unique_chat.append(x)
                else:
                    pass
            else:
                unique_chat.append(x)

    # print(unique_chat)
    return (unique_chat)

def inbox(request):
    try:
        userdetails = signmod.objects.get(username = request.session["username"])
        newmessage = chatmod.objects.filter(r2uid_id =  userdetails.uid, bell_seen = False).count()
        userlog = True
    except Exception as e:
        userlog = False
        request.session["redirect"] = "/chatroom/"
        return redirect("/login/")

    else:
        all_messages = chatmod.objects.filter(Q(r2uid_id = userdetails.uid) | Q(r1uid_id = userdetails.uid)).order_by("-text_time")
        dat = chatmod.objects.filter(r2uid_id = userdetails.uid).values("r1uid_id").annotate(recentm = Max("text_time"))
        # print(all_messages)
        # all_message = chatmod.objects.filter(Q(r2uid_id = userdetails.uid) | Q(r1uid_id = userdetails.uid)).latest()
        # print(all_message)

        all_messages = db_unique(all_messages)
        return render(request , "chatroom/inbox.html" , context = {"all_messages":all_messages , "userdetails":userdetails , "newmessage":newmessage , "userlog":userlog})


def chatrm(request , chat_user):
    try:
        userdetails = signmod.objects.get(username = request.session["username"])
        chats = chatmod.objects.filter(Q(r1uid_id = userdetails.uid , r2uid_id = chat_user) | Q(r1uid_id = chat_user , r2uid_id = userdetails.uid)).order_by("text_time")
        check_bell = chatmod.objects.filter(r2uid_id =  userdetails.uid, bell_seen = False)
        check_bell.update(bell_seen = True)
        ch_user = signmod.objects.get(uid = chat_user)
        userlog = True
    except Exception as e:
        userlog = True
        request.session["redirect"] = "/chatroom/{}/".format(chat_user)
        return redirect("/login/")

    else:
        return render(request , "chatroom/messages.html" , context = {"userdetails":userdetails , "chats":chats , "receiver":ch_user , "userlog":userlog})

# update chats
def updatechats(request):
    if request.method == "POST":
        try:
            receiver = int(request.POST["re"])
            msg = request.POST["msg"]
            id = signmod.objects.get(username = request.session["username"]).uid

        except Exception as e:
            # request.session["redirect"] = "/chatroom/updatechats/"
            receiver = int(request.POST["re"])
            return redirect("/chatroom/{}/#frm".format(receiver))

        else:
            chatmod.objects.create(text_message = msg , r1uid_id = id, r2uid_id = receiver , bell_seen = False)
            return redirect("/chatroom/{}/#frm".format(receiver))
    else:
        pass



def adminpanel(request):
    try:
        userinfo = signmod.objects.get(username = request.session["username"])
    except Exception as e:
        return redirect("/login/")
    else:
        if userinfo.is_admin:
            feeds = fd.objects.all()
            return render(request , "home/admin.html" , context = {"feeds":feeds , "userinfo":userinfo})
        else:
            return redirect("/chatroom/")
