from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Signup as signmodel
from django.contrib.auth.hashers import make_password
import json

from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Signup
import smtplib as sm ,string,random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth.hashers import check_password,make_password
from .models import Recoverdata

def profileview(request):
    if request.method == "GET":
        try:
            mydetails = sp.objects.get(username = request.session['username'])
            newmessage = chtb.objects.filter(r2uid_id =  mydetails.uid, bell_seen = False).count()
        except Exception as e:
            request.session["redirect"] = "/profile/"
            return redirect("/account/login/")
        else:
            return render(request , "uprofile/uprofile.html" , context = {"mydetails":mydetails , "newmessage":newmessage})

def update_profile(request):
    if request.method == "POST":
        try:
            edit_user_details = sp.objects.get(username = request.session['username'])
            try:
                edit_user_details.profilepic=request.FILES["profile"]
            except Exception as e:
                print(f"{e}\n\n\n\n\n")
            edit_user_details.email = request.POST["email"]
            edit_user_details.username = request.POST["username"]
            edit_user_details.hobby = request.POST["language"].title()
            edit_user_details.save()
            request.session["username"] = request.POST["username"]
        except Exception as e:
            return redirect("/profile/")
        else:
            return redirect("/profile/")
    else:
        return redirect("/profile/")

def changepassword(request):
    logger = False
    try:
        userinfo = sp.objects.get(username = request.session["username"])
    except Exception as e:
        return redirect("/login/")
    else:
        newpass = request.POST["password"]
        confirm = request.POST["confirmpassword"]
        if newpass ==confirm:
            userinfo.password = make_password(newpass)
            userinfo.save()
            password_status = "Password changed sucessfully."
            logger = True
        else:
            password_status = "Pasword not changed. Please try again"
            logger = False

        logger = json.dumps({"logger":True,"password_status":password_status})
        return HttpResponse(logger , content_type = "application/json")

def password_master(pass1,pass2):
    if pass1==pass2:
        return True
    else:
        return False

def signup(request):
    data_logger = dict()
    bugs = dict()
    data_logger["errors"] = True
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        hobby = request.POST['hobby']
        try:
            profilepic = request.FILES['profilepic']
        except Exception as e:
            bugs["profilevalid"] = "Missing profilepic"
            data_logger["fields"] = json.dumps(bugs)
        passwordflag = password_master(pass1 , pass2)
        try:
            signmodel.objects.get(username = username)
        except Exception as e:
            try:
                signmodel.objects.get(email = email )
            except Exception as e:
                if passwordflag:
                    password = make_password(request.POST['pass1'])
                    signmodel.objects.create(username = username , email = email , password = password ,
                    hobby = hobby, profilepic = profilepic)
                    data_logger["redirect"] = "/account/"
                    data_logger["errors"] = False
                    data_logger = json.dumps(data_logger)
                else:
                    bugs["passwordvalid"] = "Password not correct"
                    data_logger["fields"] = json.dumps(bugs)
                    data_logger = json.dumps(data_logger)
            else:
                bugs["emailvalid"] = "Email does not exists"
                data_logger["fields"] = json.dumps(bugs)
                data_logger = json.dumps(data_logger)
        else:
            bugs["usernamevalid"] = "User exists"
            data_logger["fields"] = json.dumps(bugs)
            data_logger = json.dumps(data_logger)
        return HttpResponse(data_logger ,  content_type="application/json")
    else:
        return render(request , "signup/signup.html")


# username is in use?
def userauthentication(request):
    try:
        uname = request.POST['username']

    except Exception as e:
        pass
    else:
        try:
            signmodel.objects.get(username = uname)
        except Exception as e:
            return HttpResponse("false")
        else:
            return HttpResponse("true")
# email is in use?
def emailauthentication(request):
    try:
        email = request.POST['email']
    except Exception as e:
        pass
    else:
        try:
            signmodel.objects.get(email = email)
        except Exception as e:
            if v.validate_email(email):
                return HttpResponse("false")
            else:
                return HttpResponse("Email not found")
        else:
            return HttpResponse("true")

def login(request):
    if request.method == "POST":
        error_log = list()
        username = request.POST['username']
        password = request.POST['password']
        try:
            userinfo = Signup.objects.get(username = username)
            username = userinfo.username
        except Exception as e:
            error_log.append(" Wrong credentials")
            return render(request , "login/login.html" , context = {"error_log" : error_log})
        else:
            if check_password(password , userinfo.password):
                # add username to the session
                request.session["username"] = username
                request.session['items'] = list()
                request.session["loginstatus"] = True

                try:
                    red_req = request.session["redirect"]
                    del request.session["redirect"]
                except Exception as e:
                    # set the sessions expiry date
                    request.session.set_expiry(0)
                    # redirect user to home page
                    return redirect("/")
                else:
                    return redirect("{}".format(red_req))
            else:
                error_log.append("Wrong credentials")
                return render(request , "login/login.html" , context = {"error_log" : error_log})
    else:
        try:
            request.session["username"]
        except Exception as e:
            return render(request , "login/login.html")

        else:
            return redirect("/")


def forgotcredetials(request):

    bug_hunter = []

    if request.method == "POST":
        try:
            lostuser = request.POST['email']

        except Exception as e:
            bug_hunter.append("Invalid input")
            return render(request , "login/forgot.html" , context = {"error":bug_hunter})

        else:
            try:
                userdata = Signup.objects.get(email = lostuser)
            except Signup.DoesNotExist as e:
                bug_hunter.append("Email not registered with us")
                return render(request , "login/forgot.html" , context = {"error":bug_hunter})
            else:
                if v.validate_email(lostuser):
                    hashcode = string.digits + string.ascii_letters + string.digits + string.digits
                    hashcode = "".join([random.choice(hashcode) for value in range(10)])
                    sender = "anornymous99@gmail.com"
                    receiver = lostuser
                    # message = """From: %s
                    # To: %s,
                    # Content-Type:text/html,
                    # Mime-version:1.0,
                    # Content-disposition: text,
                    # Subject:Vibes reset password is: %s,
                    # """%("devcodesv1@gmail.com",receiver , hashcode)
                    message = "Your recovery code is <strong>%s </strong><a href='devcodes.herokuapp.com/login/updatereset/'> reset link</a>"%hashcode
                    mess = MIMEMultipart("alternatives")
                    mess["From"] = "devcodesv1@gmail.com"
                    mess["To"] = receiver
                    mess["Subject"] = "Devcodes recovery code."
                    message = MIMEText( message, "html")
                    mess.attach(message)
                    try:
                        obj=sm.SMTP('smtp.gmail.com', 587)
                        obj.starttls()
                        obj.login("devcodesv1@gmail.com","admin@devcodesv1.1")
                        obj.sendmail(sender,receiver,mess.as_string())
                        obj.close()
                    except Exception as error:
                        print("Error: {}".format(error))
                        bug_hunter.append("Connection could not be established")
                        # bug_hunter.append(error)
                        return render(request , "login/forgot.html" , context = {"error":bug_hunter})

                    else:
                        Recoverdata.objects.create(uid_id = Signup.objects.get(email = receiver).uid , secret_code = hashcode)
                        print("Message sent successfully to {}".format(receiver))
                        print("Exiting the mail client program")
                        return render(request , "login/thanks.html")
                else:
                    return render(request , "login/forgot.html" , context = {"error":bug_hunter})
    else:
        return render(request , "login/forgot.html" , context = {"error":bug_hunter})


def newcr(request):
    bug_hunter = list()
    if request.method=="POST":
        newpass = make_password(request.POST["password"])
        confirmnewpass = request.POST["confirmpassword"]
        secretcode = request.POST["code"]
        try:
            recpassword  = Recoverdata.objects.get(secret_code = secretcode)
            dataobj = Signup.objects.filter(uid = recpassword.uid_id)
        except (Recoverdata.DoesNotExist,Signup.DoesNotExist) as e:
            bug_hunter.append("Incorrect information provided.")
        else:
            dataobj.update(password = newpass)
            recpassword.delete()
        return redirect("/login/")
    else:
        return render(request , "login/newcreds.html" , context = {"error":bug_hunter})

def logout(request):
    # clear the session vars
    request.session.clear()
    request.session.flush()
    request.session["loginstatus"] = False
    return redirect("/")




def DashBoard(request):
    if request.method == "GET":
        try:
            mydetails = sp.objects.get(username = request.session['username'])
            newmessage = chtb.objects.filter(r2uid_id =  mydetails.uid, bell_seen = False).count()
        except Exception as e:
            request.session["redirect"] = "/profile/"
            return redirect("/login/")
        else:
            return render(request , "uprofile/uprofile.html" , context = {"mydetails":mydetails , "newmessage":newmessage})

def update_profile(request):
    if request.method == "POST":
        try:
            edit_user_details = sp.objects.get(username = request.session['username'])
            try:
                edit_user_details.profilepic=request.FILES["profile"]
            except Exception as e:
                print(f"{e}\n\n\n\n\n")
            edit_user_details.email = request.POST["email"]
            edit_user_details.username = request.POST["username"]
            edit_user_details.hobby = request.POST["language"].title()
            edit_user_details.save()
            request.session["username"] = request.POST["username"]
        except Exception as e:
            return redirect("/profile/")
        else:
            return redirect("/profile/")
    else:
        return redirect("/profile/")

def changepassword(request):
    logger = False
    try:
        userinfo = sp.objects.get(username = request.session["username"])
    except Exception as e:
        return redirect("/login/")
    else:
        newpass = request.POST["password"]
        confirm = request.POST["confirmpassword"]
        if newpass ==confirm:
            userinfo.password = make_password(newpass)
            userinfo.save()
            password_status = "Password changed sucessfully."
            logger = True
        else:
            password_status = "Pasword not changed. Please try again"
            logger = False

        logger = json.dumps({"logger":True,"password_status":password_status})
        return HttpResponse(logger , content_type = "application/json")
