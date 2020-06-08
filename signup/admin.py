from django.contrib import admin
from .models import Signup
# Register your models here.


# Cutom admin panel

class admininterface(admin.ModelAdmin):

    model = Signup
    list_display = ("email" , "username" , "hobby" , "profilepic" , "password")

admin.site.register(Signup, admininterface)
