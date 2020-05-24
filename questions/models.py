from django.db import models
from signup.models import Signup
from cloudinary.models import CloudinaryField


# The questions to answer
class Questions(models.Model):
    qid = models.AutoField(primary_key = True , serialize = True)
    quid = models.ForeignKey(Signup , related_name = "question_asker" , on_delete = models.CASCADE)
    question = models.CharField(max_length = 1025)
    time_posted = models.DateTimeField(auto_now_add = True)
    language = models.CharField(max_length = 15 , default = "Python")
    qphoto = CloudinaryField("image" , default = "")

    class Meta:
        db_table = "Questions"


# The answers class
class Answers(models.Model):
    aid = models.AutoField(primary_key = True , serialize = True)
    auid = models.ForeignKey(Signup , related_name = "question_answerer" , on_delete = models.CASCADE)
    question_to_answer = models.ForeignKey(Questions , related_name = "question_to_answer" , on_delete = models.CASCADE)
    answer = models.CharField(max_length = 255)
    time_posted = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "Answers"


class QuestionLike(models.Model):
    lid = models.AutoField(primary_key = True , serialize = True)
    Qid = models.ForeignKey(Questions , related_name = "question_liked" , on_delete = models.CASCADE)
    luid = models.ForeignKey(Signup , related_name = "Qliker" , on_delete = models.CASCADE)


    class Meta:
        db_table = "likes"
