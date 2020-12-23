from django.db import models
from userapp.models import CustomUser
from mainapp.models import *
from DjangoUeditor.models import UEditorField


# Create your models here.


class BaseOperate(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="所属用户", on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),

    class Meta:
        abstract = True


class Question(BaseOperate):
    name = models.CharField(verbose_name="问题名", max_length=20)
    question_text = UEditorField(imagePath="operateapp/questions", verbose_name="问题内容", toolbars="mini",
                                 width=400)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="文章问题", related_name="questions")

    def __str__(self):
        return self.name


class Answer(BaseOperate):
    answer_text = UEditorField(imagePath="operateapp/answers", verbose_name="回答内容", toolbars="mini", width=400)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="所属问题", related_name="answers")


