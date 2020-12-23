"""
author:skr
datetime:2020/12/1 11:35
reversion:1.0
"""

from django.contrib.auth.backends import BaseBackend
from .models import CustomUser


class CustomBackend(BaseBackend):
    # 用于校验

    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None:
            email = kwargs.get("email")
        if email is None or password is None:
            return
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            print("没有找到用户信息")
        else:
            if user.check_password(password):
                return user

    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
        return user
