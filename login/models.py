from django.db import models
from signup.models import Signup as sv
# Create your models here.
class Recoverdata(models.Model):
    id = models.AutoField(primary_key = True , serialize = True)
    uid = models.ForeignKey(sv , related_name = "recnewdb" , on_delete = models.CASCADE , default = 1)
    secret_code = models.CharField(max_length = 10 , default = [*range(10)])
