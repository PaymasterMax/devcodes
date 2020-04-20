from django import template

register = template.Library()


@register.filter("messenger")
def cont(obj1 , obj2):
    # obj1.first_user.r2uid_id == obj2.uid:

    return 0
