from django.db import models
from signup.models import Signup as sv
# Create your models here.
class recoverdata(models.Model):
    """docstring for recoverdata."""

    def __init__(self, arg):
        super(recoverdata, self).__init__()
        self.arg = arg

    id = models.AutoField(primary_key = True , serialize = True)
    uid = models.ForeignKey(sv , related_name = "recnewdb")
    secret_code = models.CharField(max_length = 10)
