from django import template
from django.utils import timezone
import time

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
