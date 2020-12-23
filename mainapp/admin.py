from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Cate)
class CateAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class DetailAdmin(admin.ModelAdmin):
    pass
