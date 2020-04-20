from django.shortcuts import render , redirect
from signup.models import Signup
from .forms import anserform
from django.db.models import Count


from .models import Questions , Answers

def questionsview(request):
    all_questions = Questions.objects.all().annotate(no_of_answers = Count("question_to_answer"))
    return render(request , "questions/questions.html" , context = {"Questions":all_questions})


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


def askquestionsview(request , Qid):
    if request.method == "POST":
        try:
            userdetails = Signup.objects.get(username = request.session["username"])
            question = request.POST["question"]
        except Exception as e:
            return redirect("/login/")

        else:
            Questions.objects.create(quid_id = userdetails.uid, question = question)
            return render(request , "questions/questions.html")
    else:
        return render(request , "questions/questions.html")


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
