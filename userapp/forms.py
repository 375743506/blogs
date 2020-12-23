"""
author:skr
datetime:2020/12/1 10:19
reversion:1.0
"""
from django.forms import widgets
from django import forms
from .models import CustomUser


class RegistForm(forms.ModelForm):
    password2 = forms.CharField(max_length=12, label="重复密码", widget=widgets.PasswordInput(attrs={
        "id": "password2",
        "class": "form-control",
        "placeholder": "请再次输入密码",
        "required": True
    }))

    class Meta:
        fields = ["email", "username", "password", "password2"]
        model = CustomUser
        widgets = {
            "email": widgets.EmailInput(attrs={
                "id": "password",
                "class": "form-control",
                "placeholder": "请输入电子邮箱",
                "required": True
            }),
            "username": widgets.TextInput(attrs={
                "id": "password",
                "class": "form-control",
                "placeholder": "请输入用户名",
                "required": True
            }),
            "password": widgets.PasswordInput(attrs={
                "id": "password",
                "class": "form-control",
                "placeholder": "请输入密码",
                "required": True
            }),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        fields = ["email", "password"]
        model = CustomUser
        widgets = {
            "email": widgets.TextInput(attrs={
                "id": "email",
                "class": "form-control",
                "placeholder": "请输入邮箱",
                "required": True
            }),
            "password": widgets.PasswordInput(attrs={
                "id": "password",
                "class": "form-control",
                "placeholder": "请输入密码",
                "required": True
            }),
        }


class ChangePasswordForm(forms.ModelForm):
    npassword = forms.CharField(max_length=12, label="新的密码", widget=widgets.PasswordInput(attrs={
        "id": "password2",
        "class": "form-control",
        "placeholder": "请输入新密码",
        "required": True
    }))
    npassword2 = forms.CharField(max_length=12, label="重复新密码", widget=widgets.PasswordInput(attrs={
        "id": "password2",
        "class": "form-control",
        "placeholder": "请再次输入密码",
        "required": True
    }))

    class Meta:
        fields = ["password"]
        model = CustomUser
        widgets = {

            "password": widgets.PasswordInput(attrs={
                "id": "password",
                "class": "form-control",
                "placeholder": "请输入当前密码",
                "required": True
            }),
        }


class ChangeForm(forms.ModelForm):
    username2 = forms.CharField(max_length=12, label="新用户名", widget=widgets.TextInput(attrs={
        "id": "username2",
        "class": "form-control",
        "placeholder": "请输入新名字",
        "required": True
    }))

    class Meta:
        fields = ["password", "username2", "email"]
        model = CustomUser
        widgets = {
            "password": widgets.PasswordInput(attrs={
                "id": "password",
                "class": "form-control",
                "placeholder": "请输入当前密码",
                "required": True
            }),
            "email": widgets.TextInput(attrs={
                "id": "email",
                "class": "form-control",
                "placeholder": "请输入邮箱",
                "required": True
            }),
        }


class ChangePicForm(forms.ModelForm):

    class Meta:
        fields = ["headpic"]
        model = CustomUser

