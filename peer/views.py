from django.shortcuts import render
from signup.models import Signup
from chatroom.models import ChatModel as chtb

def peers(request):
    all_users = Signup.objects.all()
    try:
        current_user = Signup.objects.get(username = request.session["username"])
        all_users = Signup.objects.exclude(username = request.session["username"])

    except Exception as e:
        pass
    else:
        pass

    return render(request , "peers/peers.html" , context = {"users":all_users , "user":current_user})
