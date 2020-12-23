"""
author:skr
datetime:2020/11/28 9:16
reversion:1.0
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('regist/', regist, name='regist'),
    path('center/', center, name='center'),
    path('info/', info, name='info'),
    path('logout/', logout, name='logout'),
    path('changePassword/', changePassword, name='changePassword'),
    path('change/', change, name='change'),
    path('changePic/', changePic, name='changePic'),
    path('active/<str:name>/', active, name='active'),
]
