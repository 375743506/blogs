from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    headpic = models.ImageField(verbose_name="头像", upload_to="user/headpic",
                                default='user/headpic/default.png')
    telephone = models.CharField(max_length=11, verbose_name="手机号码")
