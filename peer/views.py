from django.shortcuts import render

# Create your views here.

def peers(request):
    return render(request , "peers/peers.html")
