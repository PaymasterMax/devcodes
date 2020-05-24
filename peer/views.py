from django.shortcuts import render,redirect
from signup.models import Signup as sp
from chatroom.models import ChatModel as chtb
from django.http import HttpResponse
from itertools import chain

def peers_suggest_per_lang(userinfo):
    try:
        users = sp.objects.exclude(username = userinfo.username).filter(hobby__iexact= userinfo.hobby)
        rest_of_users = sp.objects.exclude(username = userinfo.username).exclude(hobby__iexact = userinfo.hobby)
        print("\n\n\n\n\n{}".format(users))
        users = chain(users , rest_of_users)
        print(users)
        print("\n\n\n\n\n")
    except Exception as e:
        return sp.objects.exclude(username = userinfo.username)
    else:
        return users



def peers(request):
    all_users = sp.objects.all()
    try:
        current_user = sp.objects.get(username = request.session["username"])
        all_users = peers_suggest_per_lang(current_user)
        newmessage = chtb.objects.filter(r2uid_id =  current_user.uid, bell_seen = False).count()

    except Exception as e:
        request.session["redirect"] = "/peers/"
        return redirect("/login/")

    else:
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
            no_of_results = indexed_peers.count()

        elif criteria=="language":
            indexed_peers = sp.objects.filter(hobby__icontains = searchterm).exclude(uid= current_user.uid)
            no_of_results = indexed_peers.count()

        elif criteria=="location":
            indexed_peers = sp.objects.filter(location__icontains = searchterm).exclude(uid= current_user.uid)
            no_of_results = indexed_peers.count()

        newmessage = chtb.objects.filter(r2uid_id =  current_user.uid, bell_seen = False).count()
        return render(request , "peers/peers.html" , context = {"users":indexed_peers , "user":current_user , "rlsearch":"Related search" ,"small":"search results " , "query":searchterm , "no_of_results" : no_of_results , "newmessage":newmessage})
