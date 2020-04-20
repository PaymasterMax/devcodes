from django import template
# from


register = template.Library()


@register.filter("timemodifier")
def cont(timeobj):
    print(timeobj)
    return "2hrs ago"
