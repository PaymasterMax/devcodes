from django import template
from chatroom.models import ChatModel as cht
from django.db.models import Q,Count

register = template.Library()


@register.filter("messenger")
def cont(obj1 , obj2):
    # obj1 other person
    # obj2 me
    msg = cht.objects.filter(Q(r1uid_id = obj2.uid , r2uid_id = obj1.uid) | Q(r1uid_id = obj1.uid , r2uid_id = obj2.uid)).count()
    return msg
