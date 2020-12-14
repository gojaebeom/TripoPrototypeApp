from post.models import Post
from category.models import Category
from django.shortcuts import redirect, render
from .models import CustomUser
from django.contrib import auth

# Create your views here.
def login_menu(request):
    return render(request, 'sign/login-menu.html')


def login(request):
    if request.POST:
        username = request.POST['username'];
        password = request.POST['password'];
        user = auth.authenticate(request, username=username, password=password)
        print(user)
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'sign/login.html', {'login_false': '아이디나 비밀번호가 일치하지 않습니다😥'})

    return render(request, 'sign/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def join(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email    = request.POST['username']
        nickname = request.POST['nickname']
        CustomUser.objects.create_user(username=username, password=password, email=email, nickname=nickname)

        return redirect('/')

    return render(request, 'sign/join.html')


def show(request, id):
    user_detail = CustomUser.objects.get(id=id)
    category_list = Category.objects.all().filter(user_id=id)
    post_list = Post.objects.all().filter(user_id=id)
    print(category_list)
    return render(request, 'user/show.html', context={'user_detail':user_detail,'category_list':category_list, 'post_list':post_list})


def update_nickname(request):
    if not request.user.is_authenticated:
        return redirect('/error/403')
    if request.user.nickname:
        return redirect('/')


    return render(request, 'sign/update-nickname.html')

def edit_nickname(request, id):
    if not request.user.is_authenticated:
        return redirect('/error/403')
    if request.POST:
        user = CustomUser.objects.get(id=id)
        user.nickname = request.POST['nickname']
        user.save()
        return redirect('/')
