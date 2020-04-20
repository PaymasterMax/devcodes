from django import template


register = template.Library()


@register.filter("likey")
def liked(curuid , qidobj):
    controller = False

    # look for the match
    for x in qidobj.question_liked.all():
        # Test if the current user has liked this Queation
        if curuid == x.luid_id:
            controller = True
            break
            
    return controller
