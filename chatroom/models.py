from django.db import models
from account.models import Signup as signupobj

class ChatModel(models.Model):
    aid = models.AutoField(primary_key = True , serialize = True)
    text_time = models.DateTimeField(auto_now_add = True)
    text_message = models.CharField(max_length = 1024 , default = "")
    bell_seen = models.BooleanField()
    r1uid = models.ForeignKey(signupobj , related_name = "first_user" , on_delete = models.CASCADE)
    r2uid = models.ForeignKey(signupobj , related_name = "second_user" , on_delete = models.CASCADE)

    class Meta:
        db_table = "Chats"
        get_latest_by = "text_time"

# feedback
class FeedBack(models.Model):
    fid = models.AutoField(primary_key = True ,  serialize = True)
    feedback_sender = models.EmailField(max_length = 40 , default = "Anornymous@gmail.com")
    feedback = models.TextField(max_length = 400 , default = "")
    post_time = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "FeedBack"
