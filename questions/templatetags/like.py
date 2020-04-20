from django import template


register = template.Library()


@register.filter("likey")
def liked(curuid , qidobj):
    for x in qidobj.question_liked.all():
        # Test if the current user has liked this Queation
        if curuid == x.luid_id:
            return True

        else:
            return False
