from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.


class Cate(models.Model):
    name = models.CharField(max_length=100, verbose_name="类别")
    desc = models.TextField(verbose_name="类别描述", default="")

    def __str__(self):
        return self.name


class Article(models.Model):
    aname = models.CharField(verbose_name="文章名字", max_length=100, default="新文章")
    content = UEditorField(imagePath="mainapp/articles", verbose_name="文章内容")
    read_num = models.IntegerField(verbose_name="阅读数")
    adesc = models.TextField(verbose_name="文章描述", default="")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    mainImg = models.ImageField(upload_to='main/img', default='main/img/default.png', verbose_name="主图")
    cate = models.ForeignKey(Cate, on_delete=models.CASCADE, verbose_name="所属类别", related_name='articles')

    def __str__(self):
        return self.aname

    def prev(self):
        articles = self.cate.articles.all()
        articleslist = list(articles)
        index = articleslist.index(self)
        return articleslist[index-1]

    def next(self):
        articles = self.cate.articles.all()
        articleslist = list(articles)
        index = articleslist.index(self)
        return articleslist[index + 1]
