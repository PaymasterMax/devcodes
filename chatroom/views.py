from django.shortcuts import render,redirect
from django.http import JsonResponse
from signup.models import Signup as signmod
from .models import ChatModel as chatmod , FeedBack as fd
from django.db.models import Q,Max

def db_unique(db_obj , curr_user):
    unique_chat = list()
    for x in db_obj:
        x1 , x2 = x.r1uid_id , x.r2uid_id
        # x1  not me
        if x1 !=curr_user:
            if x1 not in [value.r1uid_id for value in unique_chat] and x1 not in [value.r2uid_id for value in unique_chat]:
                unique_chat.append(x)
        else:
            # x1 is me
            if x2 not in [value.r2uid_id for value in unique_chat] and x2 not in [value.r1uid_id for value in unique_chat]:
                unique_chat.append(x)

    return (unique_chat)


def inbox(request):
    try:
        try:
            userdetails = signmod.objects.get(username = request.session["username"])
            newmessage = chatmod.objects.filter(r2uid_id =  userdetails.uid, bell_seen = False).count()
            userlog = True
        except Exception as e:
            print("\n\n\ntop{}".format(userdetails))
            userlog = False
            request.session["redirect"] = "/chatroom/"
            return redirect("/login/")

        else:
            all_messages = chatmod.objects.filter(Q(r2uid_id = userdetails.uid) | Q(r1uid_id = userdetails.uid)).order_by("-text_time")
            print("\n\n\nfirst")
            all_messages = db_unique(all_messages , userdetails.uid)
            return render(request , "chatroom/inbox.html/" , context = {"all_messages":all_messages , "userdetails":userdetails , "newmessage":newmessage , "userlog":userlog})
    except Exception as e:
        print("\n\n\n\n\nHello{}".format(3))
    else:
        pass


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
        if chat_user==userdetails.uid:
            return redirect("/chatroom/")
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
            feeds = fd.objects.all().order_by("-post_time")
            return render(request , "home/admin.html" , context = {"feeds":feeds , "userinfo":userinfo})
        else:
            return redirect("/chatroom/")


def deletechat(request , chtid, chat_user):
    try:
        request.session["username"]
    except Exception as e:
        request.session["redirect"] = "/chatroom/{}/#frm/".format(chat_user)
        return redirect("/login/")
    else:
        chatmod.objects.get(aid = chtid).delete()
        return redirect("/chatroom/{}/#frm/".format(chat_user))


def updatemessage(request):
    try:
        usercreds = signmod.objects.get(username = request.session["username"])
    except Exception as e:
        pass
    else:
        all_messages = chatmod.objects.filter(Q(r2uid_id = usercreds.uid) | Q(r1uid_id = usercreds.uid) , bell_seen = False).order_by("-text_time")
        all_messages = db_unique(all_messages , usercreds.uid)
        all_messages = {"all_messages":all_messages}
    return JsonResponse(all_messages)

def check_new_message(request):
    return 10
