"""
author:skr
datetime:2020/12/2 16:21
reversion:1.0
"""

from haystack import indexes
from .models import Article, Cate
from django.shortcuts import get_list_or_404


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    cates = get_list_or_404(Cate)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
