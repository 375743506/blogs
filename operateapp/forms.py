"""
author:skr
datetime:2020/12/1 15:10
reversion:1.0
"""
from django.forms import widgets
from django import forms
from .models import *


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["name", "question_text"]
        widgets = {
            "name": widgets.TextInput(attrs={
                "id": "name",
                "class": "form-control",
                "placeholder": "请输入问题名字",
                "required": True
            })
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["answer_text"]
