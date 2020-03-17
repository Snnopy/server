#coding=utf-8
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import *

# Create your views here.
def index_view(request):
    #获取当前请求方式
    m = request.method
    if m=='GET':
        return render(request,'register.html')
    else:
        #获取请求参数
        name = request.POST.get('uname')
        gdr = request.POST.get('ugdr')
        pwd = request.POST.get('upwd')
        phone = request.POST.get('uphone')
        status = request.POST.get('ustatus')

        if name and pwd and gdr and phone and status:
            c = User.objects.filter(uname=name).count()
            d = User.objects.filter(uphone=phone).count()
            if c == 1 :
                return HttpResponse('name registered') #已被注册
            elif d == 1:
                return HttpResponse('phone registered')  # 已被注册
            else:
                # 创建模型对象
                user=User(uname=name,upwd=pwd,ugdr=gdr,uphone=phone,ustatus=status)
                #插入数据库
                user.save()
                return HttpResponse('success') #注册成功
        return HttpResponse('incomplete') #未输入完整信息


def show_view(request):
    m = request.method
    if m == 'GET':
        return render(request, 'show.html')
    else:
        # 获取请求参数
        name = request.POST.get('uname')
        c = User.objects.get(uname=name)
        # 转为字典类型
        info = model_to_dict(c)
        res={
            'ugdr':info['ugdr'],
            'uphone':info['uphone'],
            'ustatus':info['ustatus']
        }
        return JsonResponse(res)


def login_view(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        #获取请求数据
        name=request.POST.get('uname')
        pwd=request.POST.get('upwd')
        #查询数据库
        if name and pwd:
            c=User.objects.filter(uname=name,upwd=pwd).count()
            if c==1:
                t = User.objects.get(uname=name)
                info = model_to_dict(t)
                # 转为字典类型
                return HttpResponse(info['ustatus'])

        #判断是否登录成功
        return HttpResponse('false')


def reset_view(request):
    if request.method=='GET':
        return render(request,'reset.html')
    else:
        #获取请求数据
        phone=request.POST.get('uphone')
        pwd=request.POST.get('upwd')
        #查询数据库
        if phone and pwd:
            c=User.objects.filter(uphone=phone).count()
        #如果电话号码不匹配，提示无法修改密码
            if c==1:
                User.objects.filter(uphone=phone).update(upwd=pwd)
                return HttpResponse('success')
        return HttpResponse('fail')


'''
运行本地服务器
python manage.py runserver 192.168.1.106:8000
'''