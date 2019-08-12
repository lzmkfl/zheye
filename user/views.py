from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from zheyes.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json
from user.verify import *

def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('zheyes:index'))

@csrf_exempt
def register(request):
    """Register a new user."""
    name = request.POST['username']
    nickname = request.POST['nickname']
    phone = request.POST['mobile']
    pwd = request.POST['password']
    pwd2 = request.POST['password2']
    sexget = request.POST['sex']
    if sexget == '男':
        sex = False
    else:
        sex = True
    name_dic = verify_username(name)
    phone_dic = verify_phone(phone)
    pwd_dic = verify_pwd(pwd, pwd2)
    dictMerged = dict(name_dic, **phone_dic, **pwd_dic)
    if dictMerged['phone'] == '' and dictMerged['name'] == '' and dictMerged['pwd'] == '':
        user = User()
        user.username = name
        user.nickname = nickname
        user.mobile = phone
        user.password = pwd
        user.sex = sex
        user.save()
    return HttpResponse(json.dumps(dictMerged))

@csrf_exempt
def login(request):
    if request.method == 'POST':
            name = request.POST['username']
            pwd = request.POST['password']
            user_set =User.objects.filter(username=name, password=pwd)
            client = User()
            for u in user_set:
                client = u
            if client.username:
                request.session['client'] = client
                # serialize('json',client)
                return HttpResponse('ok')
            else:
                return HttpResponse('用户名或密码输入错误')
    else:
        return render(request, 'users/login_reg.html', locals())