from django.shortcuts import render , redirect
from signup.models import Signup
from .forms import anserform
from django.db.models import Count


from .models import Questions , Answers , QuestionLike as qlike

def questionsview(request):
    try:
        userdetails = Signup.objects.get(username = request.session["username"])
    except Exception as e:
        return redirect("/login/")

    else:
        all_questions = Questions.objects.all().annotate(no_of_answers = Count("question_to_answer")).order_by("-time_posted")
        return render(request , "questions/questions.html" , context = {"Questions":all_questions , "mydetails":userdetails})


def answersview(request , Qid):
    answers_form = anserform()

    allanswers = Answers.objects.filter(question_to_answer_id = Qid)
    question_info = Questions.objects.get(qid = Qid)

    try:
        userdetails = Signup.objects.get(username = request.session["username"])
    except Exception as e:
        return render(request , "questions/answers.html" , context = {"userdetails":"userdetails" , "answers_form":answers_form , "Qid":Qid , "allanswers":allanswers , "question_info":question_info })

    else:
        return render(request , "questions/answers.html" , context = {"userdetails":userdetails , "answers_form":answers_form , "Qid":Qid , "allanswers":allanswers , "question_info":question_info })


def askquestionsview(request):
    if request.method == "POST":
        try:
            userdetails = Signup.objects.get(username = request.session["username"])
            questionlang = request.POST["language"]
            question = request.POST["question"]
        except Exception as e:
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
            print("\n\n\n\n{}".format(e))
            return redirect("/login/")

        else:
            Answers.objects.create(auid_id = userdetails.uid , question_to_answer_id = Qid , answer = answerquery)
            return redirect("/questions/answers/{}".format(Qid))

    else:
        questionsview(request)



# update likes
def updatelikes(request):
    try:
        userdetails = Signup.objects.get(username = request.session['username'])
    except Exception as e:
        return redirect("/login/")

    else:
        qlike.objects.create(Qid_id = request.POST["Qid"] , luid_id = userdetails.uid)
        return redirect("/questions/answers/{}".format(1))
