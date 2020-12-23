"""
author:skr
datetime:2020/11/28 9:16
reversion:1.0
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('r_order/', index2, name='index2'),
    path('article/<int:id>', article, name="article"),
    path('cate/<int:id>', cate, name="cate"),
    path('no_do_it/', no_do_it, name="no_do_it"),
    path('page_order/', page_order, name='page_order'),
    path('m_about/', m_about, name="m_about"),
]
