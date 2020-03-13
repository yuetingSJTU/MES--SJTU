from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .Serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions

# Create your views here.

import hashlib


def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


class login_view(APIView):
    def post(self, request, format=None):
        # 获取表单提交的邮箱密码
        username = request.data.get("username")
        pwd = request.data.get("password")
        # 判断邮箱、密码是否存在
        if username and pwd:
            # 根据邮箱判断 从数据库中查询这个对象是否存在
            user = User.objects.filter(username=username).first()
            if user:
                # 将前端获取到的密码加密，同数据库进行验证
                if pwd == user.password:
                    return Response(status=status.HTTP_200_OK)
                return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)  # 没有信息


class register_view(APIView):
    def post(self,request,format=None):
        # 获取表单中的注册信息
        username = request.data.get("username")
        password = request.data.get("password")
        # 判断注册信息是否齐全
        if username and password:
            serializer = indexSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)  # 注册成功
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)  # 没有信息
