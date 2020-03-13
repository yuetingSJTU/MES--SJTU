from django.db import models
from django.contrib import admin

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, verbose_name="用户名")
    password = models.CharField(max_length=50, verbose_name="密码")

    class Meta:
        verbose_name = verbose_name_plural = "信息"


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    fields = ('username', 'password')


admin.site.register(User, UserAdmin)