from django.shortcuts import render
from signup.models import Signup as sp
from chatroom.models import ChatModel as chtb
from django.http import HttpResponse

def peers(request):
    all_users = sp.objects.all()
    try:
        current_user = sp.objects.get(username = request.session["username"])
        all_users = sp.objects.exclude(username = request.session["username"])
        newmessage = chtb.objects.filter(r2uid_id =  current_user.uid, bell_seen = False).count()

    except Exception as e:
        pass
    else:
        pass

    return render(request , "peers/peers.html" , context = {"users":all_users , "user":current_user , "newmessage":newmessage})


def locatepeers(request):
    try:
        searchterm = request.GET["peer"]
        criteria = request.GET['critrion']
        current_user = sp.objects.get(username = request.session["username"])

    except Exception as e:
        pass

    else:

        if criteria=="username":
            indexed_peers = sp.objects.filter(username__icontains = searchterm).exclude(uid= current_user.uid)

        elif criteria=="language":
            indexed_peers = sp.objects.filter(hobby__icontains = searchterm).exclude(uid= current_user.uid)

        elif criteria=="email":
            indexed_peers = sp.objects.filter(email__icontains = searchterm).exclude(uid= current_user.uid)

        elif criteria=="location":
            indexed_peers = sp.objects.filter(location__icontains = searchterm).exclude(uid= current_user.uid)

        else:
            indexed_peers = sp.objects.filter(pnumber__icontains = searchterm).exclude(uid= current_user.uid)

        return render(request , "peers/peers.html" , context = {"users":indexed_peers , "user":current_user})
