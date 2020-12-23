from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import *
from operateapp.forms import *
from django.core.paginator import Paginator, Page


# Create your views here.


def index(request):
    # num = {"a1":"a1","a2":"a2","a3":"a3","a4":"a4","a5":"a5",}
    cates = get_list_or_404(Cate)
    articles = get_list_or_404(Article)
    c_articles = Article.objects.all().order_by("-create_time")
    r_articles = Article.objects.all().order_by("-read_num")
    pageNum = request.GET.get("pagenum", 1)
    paginator = Paginator(c_articles, 5)
    page = paginator.get_page(pageNum)
    htmlname = "index"
    return render(request, "index.html", locals())


def index2(request):
    cates = get_list_or_404(Cate)
    articles = get_list_or_404(Article)
    c_articles = Article.objects.all().order_by("-create_time")
    r_articles = Article.objects.all().order_by("-read_num")
    pageNum = request.GET.get("pagenum", 1)
    paginator = Paginator(r_articles, 5)
    page = paginator.get_page(pageNum)
    return render(request, "index2.html", locals())


def article(request, id):
    article = get_object_or_404(Article, id=id)
    qf = QuestionForm()
    af = AnswerForm()
    return render(request, "article.html", locals())


def cate(request, id):
    cates = get_list_or_404(Cate)
    cate = get_object_or_404(Cate, id=id)
    return render(request, "cate.html", locals())


# def cate2(request, id):
#     cates = get_list_or_404(Cate)
#     cate = get_object_or_404(Cate, id=id)
#     c_articles = cate.articles.objects.all().order_by("-create_time")
#     r_articles = cate.articles.objects.all().order_by("-read_num")
#     return render(request, "cate2.html", locals())

def no_do_it(request):
    return render(request, "no_do_it.html", locals())


def page_order(request):
    c_articles = Article.objects.all().order_by("-create_time")

    # Paginator中的方法
    # validate_number 验证页码是否有效
    # get_page 获取指定页内容 等同page
    # count 返回所有带分页对象的总数
    # num_pages 返回有几个分页
    # page_range 返回页码列表  1 2 3...

    # Page中的方法
    # has_next是否有下一页
    # has_previous是否有上一页
    # has_other_pages 是否有其他页
    # next_page_number 下一页页码
    # previous_page_number 上一页页码
    # start_index 当前页第一个对象的索引

    pageNum = request.GET.get("pagenum", 1)
    paginator = Paginator(c_articles, 3)
    page = paginator.get_page(pageNum)
    return render(request, "page.html", locals())
    # return redirect(reverse("mainapp:index", args=(page,)))


def m_about(request):
    return render(request, "m_about.html", locals())
