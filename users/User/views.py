from django.shortcuts import render,HttpResponse,redirect
from User.models import login_info
from User.models import user_info

# Create your views here.

loginFlag = False

def index(request):
    return render(request,'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if check_passwd(username,password):
            loginFlag = True
            return redirect(show)
        else:
            html = '''
                    <p>请检查用户名密码是否正确<p>
                    <a href='/login/'>返回登录<a>
                '''
            return HttpResponse(html)
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':

        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        confirmpasswd = request.POST.get('confirmPwd',None)
        age = request.POST.get('age',None)
        address = request.POST.get('address',None)
        sex = request.POST.get('sex',None)

        if password == confirmpasswd:
            if add_loginInfo(username,password):
                add_userInfo(username,age,address,sex)
                html = '''
                        <p>注册成功<p>
                        <a href='/login/'>返回登录<a>
                    '''
                return HttpResponse(html)
            else:
                html = '''
                            <p>用户名已被注册，请重新输入用户名<p>
                            <a href='/register/'>返回注册<a>
                        '''
                return HttpResponse(html)
        else:
            html = '''
                <p>密码不一致，请重新输入<p>
                <a href='/register/'>返回注册<a>
            '''
            return HttpResponse(html)
    else:
        return render(request,'register.html')

def show(request):
    if not loginFlag:
        return redirect(login)
    data = {}
    UserInfo = user_info.objects.all()
    data['UserInfo'] = UserInfo
    return render(request,'show.html',context=data)

def check_passwd(username,password):
    try:
        result = login_info.objects.get(username=username)
        if result.password == password:
            return True
    except:
        return False

def add_loginInfo(username,password):
    try:
        result = login_info.objects.get(username=username)
        return False
    except:
        pass
    t = login_info(username=username, password=password)
    t.save()
    return True

def add_userInfo(name,age,addr,sex):
    u = user_info(name=name,age=age,addr=addr,sex=sex)
    u.save()
