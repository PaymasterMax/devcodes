from django.shortcuts import render , redirect
from signup.models import Signup
from .forms import anserform
from django.db.models import Count
from .models import Questions , Answers , QuestionLike as qlike
from chatroom.models import ChatModel as chtb
from chatroom.models import FeedBack as fd
from django.http import JsonResponse , HttpResponse
from django.core import serializers

def questionsview(request):
    all_questions = Questions.objects.all().annotate(no_of_answers = Count("question_to_answer")).order_by("-time_posted")
    try:
        userdetails = Signup.objects.get(username = request.session["username"])
        newmessage = chtb.objects.filter(r2uid_id =  userdetails.uid, bell_seen = False).count()
        userlog = True
    except Exception as e:
        userlog = False
        # request.session["redirect"] = "/questions/"
        # return redirect("/login/")
        return render(request , "questions/questions.html" , context = {"Questions":all_questions , "userlog":userlog})

    else:
        return render(request , "questions/questions.html" , context = {"Questions":all_questions , "mydetails":userdetails , "newmessage":newmessage , "userlog":userlog})


def myquestions(request):
    try:
        userdetails = Signup.objects.get(username = request.session["username"])
        newmessage = chtb.objects.filter(r2uid_id =  userdetails.uid, bell_seen = False).count()
        userlog = True
    except Exception as e:
        userlog = False
        request.session["redirect"] = "/questions/myquestions/"
        return redirect("/login/")

    else:
        all_questions = Questions.objects.filter(quid_id = userdetails.uid).annotate(no_of_answers = Count("question_to_answer"))
        return render(request , "questions/personal.html" , context = {"Questions":all_questions , "mydetails":userdetails , "newmessage":newmessage , "userlog":userlog})


def answersview(request , Qid):
    answers_form = anserform()

    allanswers = Answers.objects.filter(question_to_answer_id = Qid)
    question_info = Questions.objects.get(qid = Qid)

    try:
        userdetails = Signup.objects.get(username = request.session["username"])
        userlog = True
    except Exception as e:
        userlog = False
        return render(request , "questions/answers.html" , context = {"userdetails":"userdetails" , "answers_form":answers_form , "Qid":Qid , "allanswers":allanswers , "question_info":question_info , "newmessage":0})

    else:
        newmessage = chtb.objects.filter(r2uid_id =  userdetails.uid, bell_seen = False).count()
        return render(request , "questions/answers.html" , context = {"userdetails":userdetails , "answers_form":answers_form , "Qid":Qid , "allanswers":allanswers , "question_info":question_info , "newmessage":newmessage , "userlog":userlog})


def askquestionsview(request):
    if request.method == "POST":
        try:
            userdetails = Signup.objects.get(username = request.session["username"])
            questionlang = request.POST["language"]
            question = request.POST["question"]
        except Exception as e:
            request.session["redirect"] = "/questions/updatequestions/"
            return redirect("/login/")

        else:
            Questions.objects.create(quid_id = userdetails.uid, question = question , language = questionlang)
            return redirect("/questions/")
    else:
        return redirect("/questions/")


def update_answers(request , Qid):

    if request.method == "POST":
        try:
            userdetails = Signup.objects.get(username = request.session['username'])
            answerquery = request.POST["answer"]

        except Exception as e:
            request.session["redirect"] = "/questions/updateanswers/{}/".format(Qid)
            return redirect("/login/")

        else:
            Answers.objects.create(auid_id = userdetails.uid , question_to_answer_id = Qid , answer = answerquery)
            return redirect("/questions/answers/{}/".format(Qid))

    else:
        return redirect("/questions/answers/{}/".format(Qid))



# update likes
def updatelikes(request):
    try:
        userdetails = Signup.objects.get(username = request.session['username'])
    except Exception as e:
        is_logged = False
        liked = "question not liked"
    else:
        Qid = request.POST["qid"]
        qlike.objects.create(Qid_id = Qid , luid_id = userdetails.uid)
        is_logged = True
        liked = "question liked"
    data = {"liked":liked,"is_logged":is_logged , "counter":Questions.objects.filter(qid = Qid).count()}
    return JsonResponse(data)


def feed(request):
    user_mail = request.POST["email"]
    feed = request.POST["feedback"]
    fd.objects.create(feedback_sender = user_mail, feedback = feed)
    return JsonResponse({"feedback":True})


def qupdater(request):
    qdata = Questions.objects.all()
    qdata = serializers.serialize('json', qdata)
    return HttpResponse(qdata, content_type="text/json-comment-filtered")



datael = """

function elementCreator(questionobj) {
  // main holder for all questions
  var person_holder = document.getElementById("person-holder");
  // one message
  var oneQuestion = document.createElement("div");
  // set the class of the qholder
  oneQuestion.setAttribute("class" , "oneQuestion");
  // oneQuestion.innerHTML = "Hello Once a question"
  person_holder.appendChild(oneQuestion)

  // create the profilepic element
  var profilepic = document.createElement("div");
  // append cloudinary file here
  profilepic.innerHTML = {% cloudinary questionobj.quid.profilepic.url className="myimg" alt=questionobj.quid.username title=question.quid.username height=200 width=100 %};
  oneQuestion.appendChild(profilepic);

  var question_container = document.createElement("div");
  // set new objects
  question_container.setAttribute("class","question-container");
  var udetailfrow = document.createElement("div");
  udetailfrow.setAttribute("class" , "user-details-first-row");
  udetailfrow.innerHTML = {{questionobj.quid.username}}   "@"{{questionobj.time_posted | timemodifier}};

  var qcontent = document.createElement("div");
  qcontent.setAttribute("class" , "question-content");
  var qtext = document.createElement("div");
  qtext.setAttribute("class" , "question-text");
  qtext.innerHTML = "Message Content";
  qcontent.appendChild(qtext);
  var qlangtag = document.createElement("div");
  qlangtag.setAttribute("class" , "languages-tagged");
  qlangtag.innerHTML = {{questionobj.language}}
  qcontent.appendChild(qlangtag);

  var replysec = document.createElement("div");
  replysec.setAttribute("class","reply-section");

  // children of replysec
  var like = document.createElement("div");
  like.setAttribute("class" , "like");
  var lkbtn = document.createElement("button");
  lkbtn.setAttribute("type","button");
  lkbtn.setAttribute("class","likebtn");
  // lkbtn.setAttribute("width","30px");
  // lkbtn.setAttribute("height","40px");
  lkbtn.setAttribute("style" , "width: 30px; height: 40px;");
  var btnimg = document.createElement("img");
  btnimg.setAttribute("src" , "{% static 'questions/images/coloredLike.svg' %}");
  btnimg.setAttribute("id" , "final");
  btnimg.setAttribute("class" , "final");
  btnimg.setAttribute("alt" , "like button");
  btnimg.setAttribute("style" , "width: 30px; height: 40px;");

  // span element
  var spancount = document.createElement("span");
  spancount.setAttribute("id" , "question{{questionobj.qid}}");
  spancount.innerHTML = {{questionobj.question_liked.count}};

  var message = document.createElement("div");
  message.setAttribute("class" , "message");
  var mimg = document.createElement("img");
  mimg.setAttribute("src" , "{% static 'questions/images/message.svg' %}");
  mimg.setAttribute("alt" , "message icon");
  message.innerHTML = {{questionobj.no_of_answers}};
  message.appendChild(mimg);

  var Click = document.createElement("div");
  Click.setAttribute("class" , "Click");
  var Clicklink = document.createElement("a");
  Clicklink.setAttribute("href" , "{% url 'questions:answers' questionobj.qid %}");
  Clicklink.innerHTML = " Click to view replies";
  Click.appendChild(Clicklink);

  lkbtn.appendChild(btnimg);
  lkbtn.appendChild(spancount);
  like.appendChild(lkbtn);
  replysec.appendChild(like);
  replysec.appendChild(message);
  replysec.appendChild(Click);
  // end of childred of replysec

  // add childre to parents
  question_container.appendChild(udetailfrow);
  question_container.appendChild(qcontent);
  oneQuestion.appendChild(question_container);
  oneQuestion.appendChild(replysec);
}"""
