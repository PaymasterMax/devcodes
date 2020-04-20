from django.forms import ModelForm , Textarea , TextInput
from .models import Answers

class anserform(ModelForm):
    class Meta:
        model = Answers
        fields = ("answer",)

        widgets = {
        "answer":Textarea(attrs = {"cols":40 , "rows":3 , "Placeholder":"Your answer" , "id":"large"}),
        }


        labels = {
        "answer":""
        }
