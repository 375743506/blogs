from django.shortcuts import render, reverse, redirect, get_list_or_404, get_object_or_404
from .models import *
from mainapp.models import Article
from .forms import *
from django.contrib.auth.views import login_required


# Create your views here.


def question(request, id):
    article = Article.objects.get(id=id)
    questions = Question.objects.all()
    return render(request, "article.html", locals())


@login_required
def addquestion(request, id):
    qf = QuestionForm(request.POST)
    if qf.is_valid():
        q = qf.save(commit=False)
        q.user = request.user
        q.article = get_object_or_404(Article, id=id)
        q.save()
        return redirect(reverse("mainapp:article", args=(id,)))
    else:
        error = "样式有误"
        return redirect(reverse("mainapp:article", args=(id,)))
    # return HttpResponse("添加成功")


def answer(request):
    return render(request, "article.html", locals())


@login_required
def addanswer(request, id):
    print("问题id", id)
    af = AnswerForm(request.POST)
    if af.is_valid():
        instance = af.save(commit=False)
        instance.user = request.user
        instance.question = get_object_or_404(Question, id=id)
        instance.save()
        return redirect(reverse("mainapp:article", args=(get_object_or_404(Question, id=id).article.id,)))
    else:
        return redirect(reverse("mainapp:article", args=(get_object_or_404(Question, id=id).article.id,)))
    # return HttpResponse("添加成功")
