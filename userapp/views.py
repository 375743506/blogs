from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from .models import *
from django.contrib.auth.views import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout as lgo, login as lgi, authenticate
from .forms import *


# Create your views here.


def login(request):
    lf = LoginForm()
    if request.method == "GET":
        return render(request, "login.html", locals())
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)
        # user = CustomUser.objects.filter(email=email, password=password).exists()
        user = authenticate(request, email=email, password=password)
        print(user)
        if user:
            if user.is_active:
                lgi(request, user)
                next = request.GET.get("next")
                if next:
                    return redirect(next)
                else:
                    return redirect(reverse("mainapp:index"))
            else:
                error = "邮箱未激活"
                return render(request, "login.html", locals())
        else:
            error = "邮箱或密码错误"
            return render(request, "login.html", locals())


def regist(request):
    rf = RegistForm()
    if request.method == "GET":
        return render(request, "regist.html", locals())
    if request.method == "POST":
        rf = RegistForm(request.POST)
        password2 = request.POST.get("password2")
        if rf.is_valid():
            r = rf.save(commit=False)
            if CustomUser.objects.filter(email=r.email).exists():
                error = "邮箱已存在"
                return render(request, "regist.html", locals())
            else:
                if r.password == password2:
                    try:
                        r.password = make_password(r.password)
                        r.is_active = False

                        from itsdangerous import TimedJSONWebSignatureSerializer
                        from blogsproject.settings import SECRET_KEY
                        util = TimedJSONWebSignatureSerializer(SECRET_KEY, expires_in=7 * 24 * 60 * 60)
                        info = util.dumps({"username": r.username}).decode("utf-8")

                        from django.core.mail import send_mail
                        from blogsproject.settings import EMAIL_HOST_USER
                        msg = f'<a href="http://192.168.11.144:8000/user/active/{info}/">点我激活</a>'
                        send_mail("激活邮件", "登录之前需要进行激活", EMAIL_HOST_USER,
                                  [r.email, "375743506@qq.com", "s18538251127@163.com"], html_message=msg)

                        r.save()
                    except Exception as e:
                        print(e, "注册失败")
                    return redirect(reverse("userapp:login"))
                else:
                    error = "两次密码不一致"
                    return render(request, "regist.html", locals())
        else:
            error = "格式有误请重新输入"
            return render(request, "regist.html", locals())


@login_required
def center(request):
    return render(request, "center.html", locals())


@login_required
def info(request):
    return render(request, "info.html", locals())


@login_required
def logout(request):
    lgo(request)
    return redirect(reverse("userapp:login"))


@login_required
def changePassword(request):
    cpf = ChangePasswordForm()
    if request.method == "GET":
        return render(request, "changePassword.html", locals())
    if request.method == "POST":
        password = request.POST.get("password")
        npassword = request.POST.get("npassword")
        npassword2 = request.POST.get("npassword2")
        check = check_password(password, request.user.password)
        if check:
            if npassword == npassword2:
                user = request.user
                user.password = make_password(npassword)
                user.save()
                lgi(request, user, backend="userapp.backends.CustomBackend")
                return redirect(reverse("userapp:center"))
        else:
            error = "当前密码输入错误"
            return render(request, "changePassword.html", locals())


@login_required
def change(request):
    cf = ChangeForm()
    if request.method == "GET":
        return render(request, "change.html", locals())
    if request.method == "POST":
        username2 = request.POST.get("username2")
        password = request.POST.get("password")
        email = request.POST.get("email")
        check = check_password(password, request.user.password)
        if check:
            user = request.user
            user.username = username2
            user.email = email
            user.save()
            return redirect(reverse("userapp:center"))
        else:
            error = "密码错误"
            return render(request, "change.html", locals())


@login_required
def changePic(request):
    cpf = ChangePicForm()
    if request.method == "GET":
        return render(request, "changePic.html", locals())
    if request.method == "POST":
        cpf = ChangePicForm(request.POST, request.FILES)
        if cpf.is_valid():
            headpic = cpf.cleaned_data["headpic"]
            user = request.user
            user.headpic = headpic
            # print(user.headpic, "=====")
            user.save()
            return redirect(reverse("userapp:center"))
        else:
            error = "格式错误"
            return render(request, "changePic.html", locals())


def active(request, name):
    from itsdangerous import TimedJSONWebSignatureSerializer
    from blogsproject.settings import SECRET_KEY
    util = TimedJSONWebSignatureSerializer(SECRET_KEY, expires_in=7 * 24 * 60 * 60)
    info = util.loads(name)

    user = get_object_or_404(CustomUser, username=info["username"])
    user.is_active = True
    user.save()
    return redirect(reverse("userapp:login"))
