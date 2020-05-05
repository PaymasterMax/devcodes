from django.db import models


# feedback

class FeedBack(models.Model):
    fid = models.AutoField(primary_key = True ,  serialize = True)
    feedback_sender = models.EmailField(max_length = 40)
    feedback = models.TextField(max_length = 400 , default = "")
    post_time = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "FeedBack"
