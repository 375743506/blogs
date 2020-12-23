"""
author:skr
datetime:2020/11/28 9:16
reversion:1.0
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('question/<int:id>', question, name='question'),
    path('addquestion/<int:id>', addquestion, name='addquestion'),

    path('answer/', answer, name='answer'),
    path('addanswer/<int:id>', addanswer, name='addanswer'),
]
