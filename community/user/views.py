from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
#패스워드 암호화 하는 라이브러리
from .models import user
from .forms import LoginForm 
# Create your views here.

def home(request):
    user_id = request.session.get('user')

    if user_id:
        pre_user = user.objects.get(pk=user_id)
        #pk 기본키
    return render(request,'home.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})
    # if request.method == 'GET':
    #     return render(request,'login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username',None)
    #     password = request.POST.get('password',None)

    #     res_data = {}
    #     if not (username and password):
    #         res_data['error'] = '모든 값을 입력해야 합니다.'
    #     else:
    #         pre_user = user.objects.get(username=username)
    #         if check_password(password, pre_user.password):
    #             #세션
    #             request.session['user'] = pre_user.id
    #             return redirect('/')
    #             #pass
    #             # 비밀번호가 일치, 로그인 처리 
    #         else:
    #             res_data['error'] = '비밀번호가 틀렸습니다.'


def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        useremail = request.POST.get('useremail',None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re-password',None)

        res_data = {}
        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        if password != re_password:
            #return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = user(
            username=username,
            useremail=useremail,
            password=make_password(password)
            )
            fcuser.save()
        return render(request,'register.html',res_data)