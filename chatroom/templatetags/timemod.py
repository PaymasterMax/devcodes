from django import template
from django.utils import timezone
import time
from chatroom.models import ChatModel as chtmd

register = template.Library()


@register.filter("timemodifier")
def cont(timeobj):
    time_lapse = int((timezone.now()-timeobj).total_seconds())

    # test for days
    if time_lapse <= 432000 and time_lapse >= 86400:

        return str(int(time_lapse/86400)) + " day(s) ago"

    elif time_lapse<86400:

        # test for hours
        if time_lapse>=3600:
            return str(int(time_lapse/3600)) + " hours ago"

            # test for minutes
        elif time_lapse<3600 and time_lapse>60:
            return str(int(time_lapse/60)) + " minutes ago"

        # test for seconds
        else:
            return str(time_lapse) + " seconds ago"


    else:
        return timeobj

@register.filter("umodifier")
def umod(send_id , my_id):
    if send_id==my_id:
        return True
    else:
        return False


@register.filter("msagecounter")
def msagecount(msguid , msguid2):
    mymessages = chtmd.objects.filter(r1uid_id = msguid , r2uid_id = msguid2)
    unread = 0
    for x in mymessages:
        if not x.bell_seen:
            unread+=1
    return unread



@register.filter("username_modifier")
def usermodifier(username):
    return username.split(" ")[0]
