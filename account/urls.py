from django.conf.urls import url
from . import views

app_name ="account"

urlpatterns = [
        url('^$' , views.login , name = 'login'),
        url("^forgot/$" , views.forgotcredetials , name = 'forgot'),
        url("^update/$" , views.update_profile , name = "update"),
        url("^dashboard/$", views.DashBoard, name = "profile"),
        url("^updatereset/" , views.newcr , name = "newcreds"),
        url('^profile/$' , views.signup , name = 'profile'),
        url('^signup/$' , views.signup , name = 'signup'),
        url("^logout/" , views.logout , name = "logout"),
        url('^userauthentication/' , views.userauthentication , name = 'userauthentication'),
        url( "^changepassword/$" , views.changepassword , name = "changepassword"),
        url('^emailauthentication/' , views.emailauthentication , name = 'emailauthentication'),
]
